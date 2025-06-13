from __future__ import annotations

import abc
import copy
import os.path
import pickle
import sys
import threading
import uuid
from collections import OrderedDict, deque
from typing import Any, Final, Optional, Callable




class NoValue:
    pass


class ExecMode(abc.ABC):
    _dump_dir: Final[str]

    def __init__(self, dump_dir: str):
        self._dump_dir = dump_dir

    def snapshot(self, env: Environment, snap_id: Optional[int]) -> None:
        #print(f"[DEBUG] Snapshotting with {len(env._msg_queue)} jobs")
        filename: str = os.path.join(self._dump_dir, f"{snap_id}_snap.pickle")
        with open(filename, "wb") as df:
            pickle.dump(env, df)

    @abc.abstractmethod
    def before_execution(self, env: Environment) -> None:
        ...

    @abc.abstractmethod
    def exec(self, env: Environment) -> None:
        ...

    @abc.abstractmethod
    def after_execution(self, env: Environment) -> None:
        ...


class ExecModeRun(ExecMode):
    def exec(self, env: Environment) -> None:
        pass

    def before_execution(self, env: Environment) -> None:
        pass

    def after_execution(self, env: Environment) -> None:
        pass


class ExecModeStmtCount(ExecMode):
    def __init__(self, dump_dir):
        super().__init__(dump_dir=dump_dir)
        self.stmts_run: int = 0

    def snapshot(self, env: Environment, snap_id: Optional[int]) -> None:
        filename: str = os.path.join(self._dump_dir, f"stmt_count_snap.pickle")
        with open(filename, "wb") as df:
            pickle.dump(env, df)

    def before_execution(self, env: Environment) -> None:
        pass

    def exec(self, env: Environment) -> None:
        self.stmts_run += 1

    def after_execution(self, env: Environment) -> None:
        #print(f"Current Threads: {env._threads}")
        env._threads = []
        self.snapshot(env, 0)


class ExecModeRecord(ExecMode):
    def __init__(self, steps: int, dump_dir: str = f"dump_{uuid.uuid4()}/"):
        super().__init__(dump_dir=dump_dir)
        self._steps: Final[int] = steps
        self._exec_steps: int = 0
        self._snap_id: int = 0

        self._src_env: Optional[Environment] = None

    def _inject_snap_mode(self, env: Environment, snap_id: int, steps: int) -> None:
        env._exec_mode = ExecModeReplay(
            steps=steps, snap_id=snap_id, dump_dir=self._dump_dir
        )

    def _snap_src(self) -> None:
        if self._src_env is not None:
            print("[DEBUG] Snapshotting\n")
            #self._src_env.print_all_jobs()

            src_env_ref = self._src_env
            src_env_ref._threads = []
            src_env_snap_id = self._snap_id - 1
            self._inject_snap_mode(src_env_ref, src_env_snap_id, steps=self._exec_steps)
            self.snapshot(env=src_env_ref, snap_id=src_env_snap_id)

    def before_execution(self, env: Environment) -> None:
        saved_threads = env._threads
        env._threads = []
        self._src_env = copy.deepcopy(env)
        env._threads = saved_threads
        self._snap_id += 1

    def exec(self, env: Environment) -> None:
        self._exec_steps += 1
        if self._exec_steps == self._steps:
       
            #env.print_all_jobs()
            self._snap_src()
            
            self._src_env = copy.deepcopy(env)
            self._snap_id += 1
            self._exec_steps: int = 0

            # Clear ios for next trace.
            env.clear_io()

    def after_execution(self, env: Environment) -> None:
        # Persist the previous state, with steps to reach this last one.
        self._snap_src()
        # Persist final env if steps were run from source.
        if self._exec_steps > 0:
            # Persist this last one, with zero steps to reach itself.
            self._src_env = copy.deepcopy(env)
            self._snap_id += 1
            self._exec_steps = 0
            self._snap_src()

            # Clear ios for next (None) trace.
            env.clear_io()


class ExecModeReplay(ExecMode):
    def __init__(self, steps: int, snap_id: int, dump_dir: str):
        super().__init__(dump_dir=dump_dir)
        self._curr_steps: int = steps
        self._snap_id = snap_id
        self.run_stmts: int = 0

    def snapshot(self, env: Environment, snap_id: Optional[int]) -> None:
        filename: str = os.path.join(self._dump_dir, f"{snap_id}_out_snap.pickle")
        with open(filename, "wb") as df:
            pickle.dump(env, df)

    def before_execution(self, env: Environment) -> None:
        # Reset starting point
        if isinstance(env.call_trace, list):
            env.trace_idx = 0

        # Clear output and message queue
        env.clear_io()

       

    def exec(self, env: Environment) -> None:
        self.run_stmts += 1
        self._curr_steps -= 1
        if self._curr_steps == 0:
            print(f"[REPLAY] Stopping replay. Snapshotting at seq_id={env.seq_id}, run_stmts={self.run_stmts}")
            self.snapshot(env, self._snap_id)
            #env.wait_for_threads()
            sys.exit()

    def after_execution(self, env: Environment) -> None:
        pass



class IOLogs:
    _io_in: Final[list[Any]]
    _io_out: Final[list[Any]]

    def __init__(self):
        self._io_in = list()
        self._io_out = list()

    def add_io_in(self, value: Any) -> None:
        self._io_in.append(value)

    def add_io_out(self, value: Any) -> None:
        self._io_out.append(value)

    def clear(self):
        self._io_in.clear()
        self._io_out.clear()


class IllegalTraceUpdateException(RuntimeError):
    next_legal_trace: Final[int]
    target_trace_idx: Final[int]
    trace_seq_id: Final[int]
    overwrite_seq_id: Final[int]

    def __init__(
        self,
        next_legal_trace: int,
        target_trace_idx: int,
        trace_seq_id: int,
        overwrite_seq_id: int,
    ):
        super().__init__(
            f"IllegalTraceUpdateException: Attempted to update the seq_id for trace index '{target_trace_idx}' "
            f"from '{trace_seq_id}' to '{overwrite_seq_id}' when the next legal trace index is '{next_legal_trace}'"
        )
        self.next_legal_trace = next_legal_trace
        self.target_trace_idx = target_trace_idx
        self.trace_seq_id = trace_seq_id
        self.overwrite_seq_id = overwrite_seq_id

class MessageQueue:
    def __init__(self):
        self._queue = deque()

    def enqueue(self, value: Any) -> None:
        self._queue.append(value)

    def dequeue(self) -> Optional[Any]:
        if self._queue:
            return self._queue.popleft()
        return None
    
    def remove_job(self, job: EvalJob) -> None:
        try:
            # print(f"Removing job: {job}")
            # print(f"MessageQueue: {self._queue}")

            self._queue.remove(job)
        except ValueError:
            print(f"[WARNING] Tried to remove non-existing job: {job}")

    def is_empty(self) -> bool:
        return not self._queue

    def __len__(self):
        return len(self._queue)


class Environment:
    _mem: OrderedDict[int, OrderedDict[str, Any]]
    stack: list[Any]
    _msg_queue: MessageQueue
    _threads: list[threading.Thread]
    
    trace_idx: int
    call_trace: list[int]

    _io_logs: Final[IOLogs]

    _exec_mode: ExecMode

    def __init__(self, exec_mode: ExecMode):
        self.trace_idx = 0
        self.call_trace = [-1]

        self._mem = OrderedDict()
        self._msg_queue = MessageQueue()
        self._threads = []
        self.stack = list()

        self._io_logs = IOLogs()

        self._exec_mode = exec_mode

    def __getstate__(self):
        state = self.__dict__.copy()
        state["_threads"] = []  # Remove active threads when pickling
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._threads = []  # Reset threads list after unpickling

    def wait_for_threads(self):
        #print(f"Current threads: {self._threads}")
        for thread in self._threads:
            thread.join()



    @property
    def seq_id(self) -> int:
        if isinstance(self.call_trace, dict):
            trace_list = self.call_trace.get(self.trace_idx, [])
            return trace_list[-1] if trace_list else -1
        return self.call_trace[self.trace_idx]


    @seq_id.setter
    def seq_id(self, seq_id: int) -> None:
        if isinstance(self.call_trace, dict):
            trace_list = self.call_trace[self.trace_idx]
            trace_list.append(seq_id)
        else:
            next_legal_trace = len(self.call_trace) - 1
            if self.trace_idx != next_legal_trace:
                raise IllegalTraceUpdateException(
                    next_legal_trace=next_legal_trace,
                    target_trace_idx=self.trace_idx,
                    trace_seq_id=self.call_trace[self.trace_idx],
                    overwrite_seq_id=seq_id
                )
            self.call_trace[self.trace_idx] = seq_id

    def _rm_mem_scope(self):
        if self.trace_idx in self._mem:
            del self._mem[self.trace_idx]

    def mem_put(self, name: str, value: Any) -> None:
        mem_scope = self._mem.get(self.trace_idx, OrderedDict())
        mem_scope[name] = value
        self._mem[self.trace_idx] = mem_scope

    def mem_update(self, name: str, value: Any) -> None:
        idx = self.trace_idx
        while idx >= 0:
            mem_scope = self._mem.get(idx, None)
            if mem_scope and name in mem_scope:
                mem_scope[name] = value
                return
            idx -= 1
        raise RuntimeError(f"No such value '{name}' in memory '{self._mem}'.")

    def mem_exists(self, name: str) -> bool:
        try:
            self.mem_get(name=name)
            return True
        except RuntimeError:
            return False

    def mem_get(self, name: str) -> Any:
        idx = self.trace_idx
        while idx >= 0:
            mem_scope = self._mem.get(idx, None)
            if mem_scope and name in mem_scope:
                return mem_scope[name]
            idx -= 1
        raise RuntimeError(f"No such value '{name}' in memory '{self._mem}'.")

    def mem_var(
        self, name: str, seq_id: int, peak_cond: Optional[Callable] = None
    ) -> Optional[Any]:
        var_name = f".{seq_id}.{name}"
        mem_scope = self._mem.get(self.trace_idx, OrderedDict())
        if var_name in mem_scope:
            return mem_scope[var_name]

        if self.stack:
            var_value = self.stack.pop()
            if peak_cond:
                should_peak = peak_cond(var_value)
                if should_peak:
                    self.stack.append(var_value)
        else:
            var_value = None

        mem_scope[var_name] = var_value
        self._mem[self.trace_idx] = mem_scope

        return var_value

    def add_trace(self, seq_id: int) -> None:
        if isinstance(self.call_trace, dict):
            if self.trace_idx not in self.call_trace:
                self.call_trace[self.trace_idx] = []
            self.call_trace[self.trace_idx].append(seq_id)
        else:
            if not self.next_trace():
                self.call_trace.append(seq_id)
            self.trace_idx += 1


    def rm_trace(self) -> None:
        if isinstance(self.call_trace, dict):
            if self.call_trace[self.trace_idx]:
                self.call_trace[self.trace_idx].pop()
        else:
            if not self.next_trace():
                self._rm_mem_scope()
                self.call_trace.pop()
            self.trace_idx -= 1


    def next_trace(self) -> bool:
        if isinstance(self.call_trace, dict):
            # No next trace in dict-based (threaded) traces
            return False
        last_idx = len(self.call_trace) - 1
        return last_idx > self.trace_idx

    def after_statement(self) -> None:
        self._exec_mode.exec(env=self)

    def before_execution(self) -> None:
        self._exec_mode.before_execution(env=self)

    def after_execution(self) -> None:
        self._exec_mode.after_execution(env=self)
        #print("Threads:")
        #print(self._threads)
        for t in self._threads:
            t.join()

    def add_io_in(self, value: Any) -> None:
        self._io_logs.add_io_in(value=value)

    def add_io_out(self, value: Any) -> None:
        self._io_logs.add_io_out(value=value)

    def clear_io(self) -> None:
        self._io_logs.clear()

    def clear_message_queue(self) -> None:
        self._msg_queue._queue.clear()    

    def enqueue_job(self, job: Callable[[], None]) -> None:
        #print(f"[DEBUG] Enqueuing job: {job}")
        self._msg_queue.enqueue(job)
        #print(f"[DEBGUG] Length of queue: {len(self._msg_queue)}")

    def print_all_jobs(self) -> None:
        print(f"Current jobs in the queue (length = {len(self._msg_queue)}) :")
        for job in list(self._msg_queue._queue):
            print(job)

    def thread_started(self, spawn_obj: "Spawn"):
        from mona.interpreter.component.spawn import Spawn
        eval_job = EvalJob(spawn_obj)
        self.enqueue_job(eval_job)
        


    def thread_done(self, spawn_obj: "Spawn"):
        from mona.interpreter.component.spawn import Spawn
        
        target_job = EvalJob(spawn_obj)
        # Remove matching job
        self._msg_queue.remove_job(target_job)

    def is_replay(self) -> bool:
        return isinstance(self._exec_mode, ExecModeReplay)

class EvalJob:
    def __init__(self, stmt):
        self.stmt_type = type(stmt).__name__
        self.seq_id = getattr(stmt, "seq_id", None)
        self.has_arg_lst = hasattr(stmt, "arg_lst")

        # For Spawn jobs
        self.stmt_block = getattr(stmt, "stmt_block", None)
        self.thread_id = getattr(stmt, "thread_id", None)
        self.thread_trace = getattr(stmt, "thread_trace", None)  # ✅ ADD THIS LINE

    def __call__(self, env):
        raise RuntimeError("EvalJob is a metadata object, not executable.")

    def __repr__(self):
        info = {"seq_id": self.seq_id}
        if self.has_arg_lst:
            info["arg_lst"] = "(ArgumentList)"
        return f"<EvalJob for ({self.stmt_type} | {info})>"
    
    def __eq__(self, other):
        if not isinstance(other, EvalJob):
            return NotImplemented
        return self.stmt_type == other.stmt_type and self.seq_id == other.seq_id

    def __hash__(self):
        return hash((self.stmt_type, self.seq_id))

    def to_dict(self):
        return {
            "stmt_type": self.stmt_type,
            "seq_id": self.seq_id,
            "has_arg_lst": self.has_arg_lst,
        }
