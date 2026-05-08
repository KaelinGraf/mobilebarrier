from __future__ import annotations
from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Inertia:
    """Rotational inertia for 2D rigid body dynamics."""
    izz: float

    def shifted(self, mass: float, displacement: float) -> Inertia:
        """Parallel-axis theorem. `displacement` is the perpendicular
        distance between the COM and the new reference axis. Use when
        composing a sub-body whose COM isn't at the parent's origin.
        """
        return Inertia(izz=self.izz + mass * displacement ** 2)

    def __add__(self, other: Inertia) -> Inertia:
        return Inertia(izz=self.izz + other.izz)
