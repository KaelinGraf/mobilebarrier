from abc import ABC,abstractmethod

import numpy as np

class Planner(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def get(self,t)->np.ndarray:
        return np.zeros(3)
