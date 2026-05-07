from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import numpy as np

from sim2d.stack.planner import Planner
from sim2d.stack.controller import Controller

if TYPE_CHECKING:
    from sim2d.physical.hardware_group import HardwareGroup


class Behaviour(ABC):
    """A self-contained closed-loop behaviour: planner + controller pointed
    at one hardware group. Behaviours are mutually-exclusive consumers of
    the hardware they target — the Supervisor picks which one is active.

    Subclass and override `is_applicable`/`is_complete` for entry/exit
    conditions, and optionally `update` for non-trivial control flow.
    """

    def __init__(self, target: "HardwareGroup", planner: Planner, controller: Controller):
        self.target = target
        self.planner = planner
        self.controller = controller

    @abstractmethod
    def is_applicable(self, t: float, estimate: np.ndarray) -> bool:
        ...

    @abstractmethod
    def is_complete(self, t: float, estimate: np.ndarray) -> bool:
        ...

    def update(self, t: float, estimate: np.ndarray) -> np.ndarray:
        reference = self.planner.get(t)
        return self.controller.update(reference, estimate)
