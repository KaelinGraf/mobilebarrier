from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class InertiaMatrix:
    """Rotational inertia for 2D rigid body dynamics."""
    izz: float

    def shifted(self, mass: float, displacement: float) -> InertiaMatrix:
        """Parallel-axis theorem. `displacement` is the perpendicular
        distance between the COM and the new reference axis. Use when
        composing a sub-body whose COM isn't at the parent's origin.
        """
        return InertiaMatrix(izz=self.izz + mass * displacement ** 2)

    def __add__(self, other: InertiaMatrix) -> InertiaMatrix:
        return InertiaMatrix(izz=self.izz + other.izz)
