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
    _global_snap_id = -1
    _snap_lock = threading.Lock()
    
    def __init__(self, steps: int, dump_dir: str = f"dump_{uuid.uuid4()}/"):
        super().__init__(dump_dir=dump_dir)
        self._steps: Final[int] = steps
        self._exec_steps: int = 0
        self._snap_id: int = 0
        self._snapshot_lock = threading.Lock()        

        self._src_env: Optional[Environment] = None

    def _inject_snap_mode(self, env: Environment, snap_id: int, steps: int) -> None:
        env._exec_mode = ExecModeReplay(
            steps=steps, snap_id=snap_id, dump_dir=self._dump_dir
        )

    def _snap_src(self, env: Environment) -> None:
        if self._src_env is not None:
            with self._snapshot_lock:

                src_env_ref = self._src_env
                src_env_ref._threads = []
                src_env_ref._msg_queue = env._msg_queue
                src_env_snap_id = ExecModeRecord.next_global_snap_id()
                src_env_ref._msg_queue = copy.deepcopy(env._msg_queue)
                self._inject_snap_mode(src_env_ref, src_env_snap_id, steps=self._exec_steps)
                print(f"[DEBUG] Snapshotting snap_id={src_env_snap_id}\n")
                self.snapshot(env=src_env_ref, snap_id=src_env_snap_id)
                #self._dump_and_verify(src_env_ref, src_env_snap_id)
    
    @classmethod
    def next_global_snap_id(cls) -> int:
        with cls._snap_lock:
            cls._global_snap_id += 1
            return cls._global_snap_id

    # check this again, not sure if correct
    def force_snapshot(self, env: "Environment") -> None:
        """
        Immediately write a snapshot of `env`, using the same bookkeeping
        we already use internally.  Safe to call from anywhere.
        """
        # Make sure the *current* env is captured too.
        self._src_env = copy.deepcopy(env)
        self._exec_steps = 0           # reset step counter
        self._snap_src(env)               # write it to disk

    def before_execution(self, env: Environment) -> None:
        saved_threads = env._threads
        env._threads = []
        self._src_env = copy.deepcopy(env)
        env._threads = saved_threads

    def exec(self, env: Environment) -> None:
        self._exec_steps += 1
    
    # chatgpt generated
    def _dump_and_verify(self, env: "Environment", snap_id: int) -> None:
        """Write the snapshot and immediately load it back to verify.
           Runs only in ExecModeRecord."""
        filename = os.path.join(self._dump_dir, f"{snap_id}_snap.pickle")

        # --- dump ---
        with open(filename, "wb") as df:
            pickle.dump(env, df)

        # --- load right back ---
        with open(filename, "rb") as df:
            restored_env: Environment = pickle.load(df)

        # --- compare / log ---
        if env._msg_queue._queue != restored_env._msg_queue._queue:
            print(
                f"[WARN] Queue mismatch after snapshot {snap_id} "
                f"(live={list(env._msg_queue._queue)}, "
                f"restored={list(restored_env._msg_queue._queue)})"
            )
        else:
            print(f"[OK]  Snapshot {snap_id} queue verified.")
    # --------------------------------------------

    def after_execution(self, env: Environment) -> None:
        # Persist the previous state, with steps to reach this last one.
        self._snap_src(env)
        # Persist final env if steps were run from source.
        if self._exec_steps > 0:
            # Persist this last one, with zero steps to reach itself.
            self._src_env = copy.deepcopy(env)
            self._exec_steps = 0
            self._snap_src(env)

            # Clear ios for next (None) trace.
            env.clear_io()
    
    def __getstate__(self):
        state = self.__dict__.copy()
        state['_snapshot_lock'] = None  # Exclude the lock
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._snapshot_lock = threading.Lock()  # Recreate lock after unpickling



class ExecModeReplay(ExecMode):
    def __init__(self, steps: int, snap_id: int, dump_dir: str):
        super().__init__(dump_dir=dump_dir)
        self._curr_steps: int = steps
        self.run_stmts: int = 0

    def snapshot(self, env: Environment, snap_id: Optional[int]) -> None:
        filename: str = os.path.join(self._dump_dir, f"{snap_id}_out_snap.pickle")
        with open(filename, "wb") as df:
            pickle.dump(env, df)

    def before_execution(self, env: Environment) -> None:
        # Reset starting point
        print("\n>>>> MESSAGE-QUEUE AT REPLAY START")
        env._msg_queue.print_all()   
        print(f"[REPLAY] thread_id={env._thread_id}  queue_head={env._queue_head()}")
        
        env.trace_idx = 0
        env.clear_io()

    def exec(self, env: Environment) -> None:
        self.run_stmts += 1
        self._curr_steps -= 1
        assert self._curr_steps >= -10, "Replay over-ran by >10 statements – possible trace divergence."

        if not env._msg_queue._queue:
            print(f"[REPLAY] Queue is empty. Stopping replay. Snapshotting at seq_id={env.seq_id}, run_stmts={self.run_stmts}")
            snap_id = ExecModeRecord.next_global_snap_id()
            self.snapshot(env, snap_id)
            sys.exit()

        # probably can remove
        if self._curr_steps == 0:
            print(f"[REPLAY] Stopping replay. Snapshotting at seq_id={env.seq_id}, run_stmts={self.run_stmts}")
            snap_id = ExecModeRecord.next_global_snap_id()
            self.snapshot(env, snap_id)
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

class UuidQueue:
    """FIFO that stores only thread-ids (UUID strings)."""

    def __init__(self) -> None:
        self._queue: deque[str] = deque()
        self._lock = threading.Lock() 

    def __getstate__(self):
        # Exclude the lock when pickling
        state = self.__dict__.copy()
        state.pop('_lock', None)
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self._lock = threading.Lock()

    def enqueue(self, thread_id: str, env: Environment) -> None:
        with self._lock:
            print(f"Enqueuing: {thread_id}")
            self._queue.append(thread_id)

            if isinstance(env._exec_mode, ExecModeRecord) and thread_id not in env._thread_envs:
                env._thread_envs[thread_id] = copy.deepcopy(env)

            # Check if snapshot condition is met
            if isinstance(env._exec_mode, ExecModeRecord):
                if len(self._queue) >= env._exec_mode._steps:
                    self.print_all()
                    env._exec_mode._snap_src(env)
                    env._exec_mode._src_env = copy.deepcopy(env)
                    env._exec_mode._snap_id += 1
                    env._exec_mode._exec_steps = 0

                    env.clear_io()
                    env.clear_message_queue()
                    env.clear_thread_envs()


    def dequeue(self, env:Environment) -> str | None:
        if self._queue:
            tid = self._queue.popleft()
            self.print_all()
            print(f"[DEBUG] Dequeued thread id: {tid}")

            if env.is_replay():
                # restore correct env
                if tid in env._thread_envs:
                    env = env._thread_envs[tid]
                    env._thread_id = tid

            return tid
        return None
    
    def enqueue_at_start(self, tid:str) -> None:
        if self._queue:
            print("adding to queue")
            self._queue.appendleft(tid)

    def remove(self, thread_id: str) -> None:
        try:
            self._queue.remove(thread_id)
        except ValueError:
            pass                        

    def clear(self) -> None:
        self._queue.clear()

    def __len__(self) -> int:
        return len(self._queue)

    def __repr__(self) -> str:
        return f"<UuidQueue {list(self._queue)}>"
    
    def print_all(self) -> None:
        if not self._queue:
            print("(queue is empty)")
            return

        print("UuidQueue contents:")
        for idx, tid in enumerate(self._queue, start=1):
            print(f"  {idx}. {tid}")

GLOBAL_MSG_QUEUE = UuidQueue()

class Environment:
    _mem: OrderedDict[int, OrderedDict[str, Any]]
    stack: list[Any]
    _msg_queue: UuidQueue
    _threads: list[threading.Thread]
    _thread_envs: dict[str, Environment] = {}
    
    trace_idx: int
    call_trace: list[int]

    _io_logs: Final[IOLogs]

    _exec_mode: ExecMode

    def __init__(self, exec_mode: ExecMode):
        self.trace_idx = 0
        self.call_trace = [-1]
        self._amt_requeues: int = 0

        self._mem = OrderedDict()
        self._msg_queue = GLOBAL_MSG_QUEUE
        self._threads = []
        self._thread_id = 0
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
        self._exec_mode.exec(self)

    def before_execution(self) -> None:
        self._exec_mode.before_execution(env=self)

    def after_execution(self) -> None:
        self._exec_mode.after_execution(env=self)
        #print("Threads:")
        #print(self._threads)
        #for t in self._threads:
        #    t.join()

    def add_io_in(self, value: Any) -> None:
        self._io_logs.add_io_in(value=value)

    def add_io_out(self, value: Any) -> None:
        self._io_logs.add_io_out(value=value)

    def clear_io(self) -> None:
        self._io_logs.clear()

    def clear_message_queue(self) -> None:
        self._msg_queue._queue.clear()  
        
    def clear_thread_envs(self) -> None:
        self._thread_envs.clear()     

    def thread_done(self, id: str):
        
        self._msg_queue.remove(id)

    def is_replay(self) -> bool:
        return isinstance(self._exec_mode, ExecModeReplay)
    
    def _queue_head(self) -> str | None:              
        return self._msg_queue._queue[0] if self._msg_queue else None

    def _can_run_now(self) -> bool:                     
        return not self.is_replay() or self._queue_head() == self._thread_id

    def _finished_node(self, tid: int) -> None:
        if isinstance(self._exec_mode, ExecModeRecord):
            self._msg_queue.enqueue(tid, self)  # UuidQueue.append
        return
    
    def _schedule_next(self, env: "Environment") -> None:                          

        tid = env._msg_queue.dequeue(env)        
        if tid is None:
            print ("Empty Queue")

        self._amt_requeues += 1
        env._thread_id = tid             