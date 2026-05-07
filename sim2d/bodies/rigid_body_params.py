import numpy as np


from core.params import Params
from physical.properties.inertia.inertia_matrix import InertiaMatrix

class RigidBodyParams(Params):
    mass:float
    inertia:InertiaMatrix




