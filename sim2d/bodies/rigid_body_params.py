from dataclasses import dataclass
import numpy as np


from core.params import Params
from physical.properties.inertia.inertia_matrix import Inertia


@dataclass
class RigidBodyParams(Params):
    mass:float
    inertia:Inertia

    def get_matrix(self)->np.ndarray:
        return np.array([
            [self.mass,0,0],
            [0,self.mass,0],
            [0,0,self.inertia.izz]
        ])
    

    @classmethod
    def from_tuple(cls,x:tuple[float,Inertia]):
        return cls(mass= x[0],inertia=x[1])

    



    




