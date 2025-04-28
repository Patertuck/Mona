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
        def thread_fn():
            #print(f"[DEBUG] Running Spawn thread for {self.seq_id}")
            
            self.stmt_block.eval(env)
            #print(f"[DEBUG] Finished Spawn thread for {self.seq_id}")

        thread = threading.Thread(target=thread_fn)
        thread.start()
        env._threads.append(thread)

