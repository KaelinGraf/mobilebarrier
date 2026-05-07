from __future__ import annotations
import numpy as np

from sim2d.stack.behaviour import Behaviour


class Cruise(Behaviour):
    """Drive toward a waypoint at cruise speed. Active when the robot is
    far enough from its goal that precision alignment isn't needed yet.
    """

    def is_applicable(self, t: float, estimate: np.ndarray) -> bool:
        raise NotImplementedError

    def is_complete(self, t: float, estimate: np.ndarray) -> bool:
        raise NotImplementedError
