from .robot import Robot
from physical_models.mecanum_kinematics import MecanumKinematics, MecanumParams
import numpy as np

class MecanumRobot(Robot):
    def __init__(self, params:MecanumParams, start_pos:np.ndarray = np.zeros(3)):
        super().__init__(params, start_pos)
        self.kinematics = MecanumKinematics(params)

    def update(self):
        #update must take in the 
        pass