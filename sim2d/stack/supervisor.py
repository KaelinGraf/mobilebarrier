from __future__ import annotations
from abc import ABC, abstractmethod
import numpy as np

from sim2d.stack.behaviour import Behaviour


class Supervisor(ABC):
    """Decides which Behaviour is active each tick.

    The default subclass `ModeSupervisor` runs one behaviour at a time and
    transitions when the active one signals `is_complete`. More elaborate
    arbiters (priority-based, safety-overriding) plug in here too.
    """

    def __init__(self, behaviours: list[Behaviour]):
        self.behaviours = behaviours
        self.active: Behaviour | None = None

    @abstractmethod
    def select(self, t: float, estimate: np.ndarray) -> Behaviour | None:
        ...


class ModeSupervisor(Supervisor):
    """Trivial single-active-behaviour FSM. Picks the first applicable
    behaviour from `behaviours` and holds it until it reports complete or
    becomes inapplicable. Good default for small behaviour sets.
    """

    def select(self, t: float, estimate: np.ndarray) -> Behaviour | None:
        if self.active is not None:
            if self.active.is_complete(t, estimate) or not self.active.is_applicable(t, estimate):
                self.active = None
        if self.active is None:
            for b in self.behaviours:
                if b.is_applicable(t, estimate):
                    self.active = b
                    break
        return self.active
