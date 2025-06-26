import threading
import copy
import uuid

from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import (
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

        new_trace_idx = str(uuid.uuid4())

        if isinstance(env.call_trace, list):
            env.call_trace = {0: env.call_trace}

        env.call_trace[new_trace_idx] = [self.seq_id]

        # Create a deep copy of the env for the thread
        thread_env = copy.deepcopy(env)
        thread_env.trace_idx = new_trace_idx
        thread_env.call_trace = copy.deepcopy(env.call_trace)
        thread_env.seq_id = 0
        thread_env.stack = []

        # Assign matching ExecMode
        if isinstance(env._exec_mode, ExecModeRecord):
            thread_env._exec_mode = ExecModeRecord(
                steps=env._exec_mode._steps,
                dump_dir=env._exec_mode._dump_dir,
            )
        elif isinstance(env._exec_mode, ExecModeReplay):
            thread_env._exec_mode = ExecModeReplay(
                steps=env._exec_mode._curr_steps,
                snap_id=env._exec_mode._snap_id,
                dump_dir=env._exec_mode._dump_dir,
            )

        else:
            thread_env._exec_mode = ExecModeRun(dump_dir=".")

        def thread_fn():
            try:
                self.stmt_block.eval(thread_env)
            finally:
                env.thread_done(self)

        env.thread_started(self)
        thread = threading.Thread(target=thread_fn)
        thread.start()
        env._threads.append(thread)
