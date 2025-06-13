import os
from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment, ExecModeRecord, ExecModeRun
import threading
import copy
import uuid

class Spawn(Component):
    def __init__(self, seq_id: int, stmt_block: StmtBlock):
        super().__init__(seq_id=seq_id)
        self.stmt_block = stmt_block

        self.thread_id = str(uuid.uuid4())
        self.thread_trace = {self.thread_id: []}  

    def _eval_body(self, env: Environment) -> None:
        env.seq_id = self.seq_id

        thread_env = copy.deepcopy(env)
        thread_env.call_trace = {self.thread_id: [self.seq_id]}
        thread_env.trace_idx = self.thread_id

        # 🔧 Clear stack to avoid pollution from parent thread
        thread_env.stack = []

        # Copy ExecMode
        if isinstance(env._exec_mode, ExecModeRecord):
            # 🔥 Use the exact same dump_dir to avoid subdirectories
            thread_env._exec_mode = ExecModeRecord(
                steps=env._exec_mode._steps,
                dump_dir=env._exec_mode._dump_dir  # <- Same path as main thread
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




