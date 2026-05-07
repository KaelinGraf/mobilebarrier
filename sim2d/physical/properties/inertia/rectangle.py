from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def rectangle(mass: float, width: float, height: float) -> InertiaMatrix:
    """Solid rectangle about its centroid: I = (1/12) m (w² + h²)."""
    return InertiaMatrix(izz=(1.0 / 12.0) * mass * (width ** 2 + height ** 2))
