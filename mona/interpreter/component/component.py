from __future__ import annotations

import abc
import pickle
import sys
import time
from typing import Final

from mona.config import DEBUG


class Component(abc.ABC):
    def __init__(self, seq_id: int):
        self.seq_id: Final[int] = seq_id

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"({self.__class__.__name__}| {str(self.__dict__)})"

    def _log_exec_point(self, env: Environment) -> str:
        return f"[{self.seq_id}] -> {env.trace_idx}, {env.call_trace}"

    def _get_decorated_components(self) -> list[Component]:
        decorated_components: list[Component] = list()
        for member in self.__dict__.values():
            if isinstance(member, Component):
                decorated_components.append(member)
            elif isinstance(member, list):
                decorated_components.extend(
                    [
                        sub_member
                        for sub_member in member
                        if isinstance(sub_member, Component)
                    ]
                )
            elif isinstance(member, dict):
                decorated_components.extend(
                    [
                        sub_member
                        for sub_member in member.values()
                        if isinstance(sub_member, Component)
                    ]
                )
        return decorated_components

    def eval(self, env: Environment) -> None:
        from mona.interpreter.component.program import Program 

        # if env.is_replay() and not env._msg_queue._queue:
        #     print("[DEBUG]queue is empty — skipping eval")
        #     return 
        
        #print(f"Current env id:{env._thread_id}, env_seq_id:{env.seq_id}, queuehead:{env._queue_head()}, self.seq_id:{self.seq_id}")
        #print(f"Current env call trace:", env.call_trace)
        # Don't execute this code point is env point to the next, as it already was.
        if self.seq_id <= env.seq_id:
            if DEBUG:
                print(f"[DEBUG] [prun] {self._log_exec_point(env)} -> {self}")
                # can probably delete
                if env.is_replay() and env._amt_requeues:
                    for _ in range(env._amt_requeues):
                        env._msg_queue.enqueue_at_start(env._thread_id)
                    env._amt_requeues = 0
            return

        # if env.is_replay() and self.seq_id > env.seq_id and not isinstance(self, Program):
        #     env._schedule_next(env)
        # Execute exactly this code point (self.seq_id == env.seq_id).
        if DEBUG:
            print(f"[DEBUG] [eval] {self._log_exec_point(env)} -> {self}")

            
        # Run sub-logic.
        self._eval_body(env)

        if not isinstance(self, Program):
            env._finished_node(env._thread_id)
            
        # Set the code point to the next (all children logic had smaller indexes).
        env.seq_id = self.seq_id

        env.after_statement()

    @abc.abstractmethod
    def _eval_body(self, env: Environment) -> None:
        ...


class CodeJumpComponent(Component, abc.ABC):
    def eval(self, env: Environment) -> None:
        env.add_trace(0)
        super().eval(env=env)
        env.rm_trace()
