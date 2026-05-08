import numpy as np

from .body import Body
from .rigid_body_params import RigidBodyParams
from physical.properties.inertia.inertia_matrix import Inertia


class RigidBody2D(Body):
    def __init__(self,params:RigidBodyParams|tuple[float,Inertia],q_zero:np.ndarray=np.zeros(3),v_zero:np.ndarray=np.zeros(3)):
        """
        Base class for 2D rigid bodies. 
        Uses semi-implicit euler integration

        Args:
            params (RigidBodyParams|tuple(float,Inertia)): Mass + inertia for wrench calculations. Can be supplied in tuple form to construct a RigidBodyParams
            q_zero (np.ndarray, optional): _description_. Defaults to np.zeros(3).
            v_zero (np.ndarray, optional): _description_. Defaults to np.zeros(3).
        """
        self.params:RigidBodyParams = params if isinstance(params,RigidBodyParams) else RigidBodyParams.from_tuple(params)
        self.m_inv = np.linalg.inv(self.params.get_matrix()) #Note, this is the mass + inertia matrix. NOT mass. mass is self.params.mass
        self.q = q_zero
        self.v = v_zero
        self._v_dot = np.zeros(3)


    def apply_wrench(self, wrench: np.ndarray) -> None:
        """
        Applies the wrench vector (expected in form np.array([fx,fy,tau_z]), saves updates for integration step)
        Note, this step explicitly does NOT apply the update

        Co-ordintae frame -> RH, y north, x east, theta CCW 

        Args:
            wrench (np.ndarray):Net forces on body [fx,fy,tau_z] 
        """
        self._v_dot += self.m_inv@wrench.transpose()

    def integrate(self, dt:float):
        """
        semi-implicit euler integration 

        Args:
            dt (float): sim delta time
        """
        v_old = self.v.copy()
        self.v += self._v_dot * dt #k+1 step
        self.q += 0.5 * (self.v + v_old) * dt #uses updated velocity
        self._v_dot = np.zeros(3)

        

    



