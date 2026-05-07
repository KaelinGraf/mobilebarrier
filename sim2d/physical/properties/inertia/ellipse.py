from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def ellipse(mass: float, semi_major: float, semi_minor: float) -> InertiaMatrix:
    """Solid ellipse about its centroid (axis perpendicular to plane):
    I = (1/4) m (a² + b²).
    """
    return InertiaMatrix(izz=0.25 * mass * (semi_major ** 2 + semi_minor ** 2))
