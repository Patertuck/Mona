import threading
import copy
import uuid

from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import (
    GLOBAL_REPLAY_STEPS,
    Environment,
    ExecModeRun,
    ExecModeRecord,
    ExecModeReplay,
)


class Spawn(Component):
    def __init__(self, seq_id: int, stmt_block: StmtBlock):
        super().__init__(seq_id=seq_id)
        self.stmt_block = stmt_block
        self.thread_id = str(uuid.uuid4())

    def _eval_body(self, env: Environment) -> None:
        if not isinstance(env._exec_mode, ExecModeReplay):
            env.seq_id = self.seq_id

        # Generate a new UUID-based trace_idx for the thread
        new_trace_idx = str(uuid.uuid4())

        # If main call_trace is a list, convert it to dict-once (shared reference)
        if isinstance(env.call_trace, list):
            env.call_trace = {0: env.call_trace}

        env.call_trace[new_trace_idx] = [self.seq_id]

        thread_env = copy.deepcopy(env)

        thread_env._msg_queue = env._msg_queue
        thread_env._thread_envs = env._thread_envs
        thread_env.call_trace = env.call_trace

        thread_env._thread_id = self.thread_id
        thread_env.trace_idx = new_trace_idx
        thread_env.seq_id = self.seq_id
        thread_env.stack = []

        if isinstance(env._exec_mode, ExecModeReplay):
            thread_env._exec_mode = env._exec_mode
            self.stmt_block.eval(thread_env)
            env.thread_done(self.thread_id)
            return

        elif isinstance(env._exec_mode, ExecModeRecord):
            record_mode = ExecModeRecord(
                steps=env._exec_mode._steps,
                dump_dir=env._exec_mode._dump_dir,
            )
            record_mode._src_env = copy.deepcopy(thread_env)
            thread_env._exec_mode = record_mode

        else:
            thread_env._exec_mode = ExecModeRun(dump_dir=".")

        def thread_fn():
            try:
                self.stmt_block.eval(thread_env)
            finally:
                env.thread_done(self.thread_id)

        thread = threading.Thread(target=thread_fn)
        thread.start()
        env._threads.append(thread)
