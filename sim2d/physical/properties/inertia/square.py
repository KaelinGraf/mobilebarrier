from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix
from sim2d.physical.properties.inertia.rectangle import rectangle


def square(mass: float, side: float) -> InertiaMatrix:
    """Solid square about its centroid: I = (1/6) m s²."""
    return rectangle(mass, side, side)
