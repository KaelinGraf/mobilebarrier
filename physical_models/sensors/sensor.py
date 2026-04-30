import numpy as np
from abc import ABC,abstractmethod
from physical_models.params import Params
from __future__ import annotations
from .measurement import Measurement


class Sensor(ABC):
    def __init__(self,params:Params,noise_model:NoiseModel=None):
        self.params = params
        self.noise_model = noise_model
        self.last_read_time = 0.0 #the last time the sensor was read, in sim time
        self.reading = None #the current reading of the sensor, in the same units as the sensor readings. Note, this is in sim time, not real time.

    @abstractmethod
    def __call__(self)->Measurement:
        pass




#The noise model is a separate class that can be used to add noise to the sensor readings. 
#This allows for more flexibility in how noise is added, and allows for different types of noise models to be used with the same sensor.
class NoiseModel(ABC):
    @abstractmethod
    def __call__(self,reading:np.ndarray)->np.ndarray:
        pass



    
    

