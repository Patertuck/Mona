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

        thread_env = copy.deepcopy(env)
        thread_env._thread_id = self.thread_id
        thread_env._msg_queue = env._msg_queue  # shared, internally synchronized
        thread_env.stack = []
        thread_env.add_trace(self.seq_id)

        # Propagate/adjust exec mode
        if isinstance(env._exec_mode, ExecModeReplay):
            thread_env._exec_mode = env._exec_mode
            try:
                self.stmt_block.eval(thread_env)
            finally:
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

        # Launch worker
        def thread_fn():
            try:
                self.stmt_block.eval(thread_env)
            except Exception as e:
                print(f"[thread {self.thread_id}] Unhandled error: {e}")
                raise
            finally:
                env.thread_done(self.thread_id)

        t = threading.Thread(target=thread_fn, daemon=True)
        t.start()
        env._threads.append(t)


