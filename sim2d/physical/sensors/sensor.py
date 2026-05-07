from __future__ import annotations
import numpy as np
from abc import ABC,abstractmethod
from .sensor_params import SensorParams
from .measurement import Measurement


class Sensor(ABC):
    def __init__(self,params:SensorParams,noise_model:NoiseModel):
        self.params = params
        self.period = 1/params.refresh_rate
        self.noise_model = noise_model
        self.last_read_time = 0.0 #the last time the sensor was read, in sim time
        self.reading = None #the current reading of the sensor, in the same units as the sensor readings. Note, this is in sim time, not real time.

    @abstractmethod
    def __call__(self)->Measurement:
        pass

    def due(self,t)->bool:
        return (t >= (self.last_read_time + self.period))





#The noise model is a separate class that can be used to add noise to the sensor readings. 
#This allows for more flexibility in how noise is added, and allows for different types of noise models to be used with the same sensor.
class NoiseModel(ABC):
    @abstractmethod
    def __call__(self,reading:np.ndarray)->np.ndarray:
        pass



    
    

