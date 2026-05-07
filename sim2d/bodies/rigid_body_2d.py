import numpy as np

from .body import Body
from .rigid_body_params import RigidBodyParams


class RigidBody2D(Body):
    def __init__(self,params:RigidBodyParams,init_pos:np.ndarray):
        self.params = params
        self.state = np.zeros(6)



