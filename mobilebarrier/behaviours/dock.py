from __future__ import annotations
import numpy as np

from sim2d.stack.behaviour import Behaviour


class Dock(Behaviour):
    """Precision alignment to a docking target. Active in the final approach
    once the robot is inside the dock-detection radius and the dock pose is
    observed with sufficient confidence.
    """

    def is_applicable(self, t: float, estimate: np.ndarray) -> bool:
        raise NotImplementedError

    def is_complete(self, t: float, estimate: np.ndarray) -> bool:
        raise NotImplementedError
