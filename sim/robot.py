from physical_models.params import Params
from abc import ABC,abstractmethod

class Robot(ABC):
    def __init__(self,params:Params)
        pass 

    @abstractmethod
    def step(self):
        pass
