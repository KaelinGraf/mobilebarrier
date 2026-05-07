from sim2d.physical.properties.inertia.inertia_matrix import InertiaMatrix


def point_mass(mass: float, distance: float) -> InertiaMatrix:
    """Point mass at perpendicular `distance` from the rotation axis:
    I = m d². Useful for compound-body composition (combine with shifted
    primitives via InertiaMatrix.__add__).
    """
    return InertiaMatrix(izz=mass * distance ** 2)
