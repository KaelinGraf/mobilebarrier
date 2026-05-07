from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def circle(mass: float, radius: float) -> InertiaMatrix:
    """Solid disk about its centroid: I = (1/2) m r²."""
    return InertiaMatrix(izz=0.5 * mass * radius ** 2)
