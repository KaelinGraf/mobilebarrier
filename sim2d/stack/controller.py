from abc import abstractmethod, ABC
import numpy as np

#base class for controllers
class Controller(ABC):
    def __init__(self,refresh_rate:float):
        self.rf = refresh_rate
        self.period = 1/refresh_rate
        self.last_time = 0.0

    def due(self,t)->bool:
        return(t>=(self.last_time + self.period))
    

    @abstractmethod
    def update(self,reference:np.ndarray,state:np.ndarray)->np.ndarray:
        return np.zeros_like(reference)
    


