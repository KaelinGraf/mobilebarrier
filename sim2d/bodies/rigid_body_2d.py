import numpy as np

from .body import Body
from physical.properties.inertia.inertia_matrix import InertiaMatrix

class RigidBody2D(Body):
    def __init__(self,inertia:InertiaMatrix,mass,init_pos:np.ndarray):
        self.inertia = inertia
        self.state = np.zeros(6)



