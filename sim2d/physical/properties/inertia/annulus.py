from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def annulus(mass: float, inner_radius: float, outer_radius: float) -> InertiaMatrix:
    """Hollow ring (uniform density) about its centroid:
    I = (1/2) m (r_inner² + r_outer²). Useful for wheel and ring shapes.
    """
    return InertiaMatrix(izz=0.5 * mass * (inner_radius ** 2 + outer_radius ** 2))
