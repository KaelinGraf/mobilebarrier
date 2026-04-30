from physical_models.sensors.measurement import Measurement
from .measurement_model import MeasurementModel
from abc import ABC,abstractmethod
import numpy as np

class StateEstimator(ABC):
    def __init__(self):
        self.state = np.zeros(8) #the state of the robot
        pass

    def predict(self,dt:float)->None: 
        #mutates internal state based on the motion model and the time step, dt, in seconds. Note, this is in sim time, not real time.
        pass

    def update(self,measurement:Measurement)->None:



