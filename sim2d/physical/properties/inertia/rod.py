from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def rod(mass: float, length: float) -> InertiaMatrix:
    """Thin rod about its centroid (axis perpendicular to length):
    I = (1/12) m L².
    """
    return InertiaMatrix(izz=(1.0 / 12.0) * mass * length ** 2)
