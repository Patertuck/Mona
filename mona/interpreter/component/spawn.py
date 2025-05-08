from mona.interpreter.component.component import Component
from mona.interpreter.component.stmt_block import StmtBlock
from mona.interpreter.environment.environment import Environment
import threading
import copy

class Spawn(Component):
    def __init__(self, seq_id: int, stmt_block: StmtBlock):
        super().__init__(seq_id=seq_id)
        self.stmt_block = stmt_block

    def _eval_body(self, env: Environment) -> None:
        # In parent, do normal seq_id update
        if env.trace_idx != len(env.call_trace) - 1:
            env.add_trace(self.seq_id)
        else:
            env.seq_id = self.seq_id

        # Make a deep copy of the env for the thread
        thread_env = copy.deepcopy(env)

        def thread_fn():
            try:
                # In the thread: add new trace
                thread_env.add_trace(self.seq_id)
                
                self.stmt_block.eval(thread_env)

                thread_env.rm_trace()  # after eval, clean up

            finally:
                env.thread_done(self)

        env.thread_started(self)  # parent enqueues the spawn job
        thread = threading.Thread(target=thread_fn)
        thread.start()
        env._threads.append(thread)
