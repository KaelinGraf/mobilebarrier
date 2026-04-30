from physical_models.params import Params
from abc import ABC,abstractmethod
import numpy as np

class Robot(ABC):
    def __init__(self,params:Params,start_pos:np.ndarray):
        self.params = params #note, params is an abstract class, so it can be any type of params, as long as it inherits from Params
        self.pos = start_pos

    @abstractmethod
    def update(self):
        pass
