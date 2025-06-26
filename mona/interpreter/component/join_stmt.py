from mona.interpreter.component.component import Component
from mona.interpreter.environment.environment import Environment, ExecModeRecord

class JoinStmt(Component):
    def __init__(self, seq_id: int, line: int):
        self.seq_id = seq_id
        self.line = line

    def _eval_body(self, env: Environment):
        if env.trace_idx != len(env.call_trace) - 1:
            env.add_trace(self.seq_id)
        else:
            env.seq_id = self.seq_id

        if isinstance(env._exec_mode, ExecModeRecord):
            env._exec_mode.force_snapshot(env)

        env.wait_for_threads()

    def __str__(self):
        return f"[Line {self.line}] join;"
