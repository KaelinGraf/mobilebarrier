from abc import abstractmethod,ABC

import numpy as np

class Body(ABC):
    def __init__(self,q:np.ndarray=np.zeros(3),v:np.ndarray = np.zeros(3)) -> None:
        """
        Base class for all bodies.
        apply_wrench and integrate must be overriden.
        Apply wrench is an accumulation step. 
        """

    @abstractmethod
    def apply_wrench(self,wrench:np.ndarray)->None:
        pass


    @abstractmethod
    def integrate(self,dt):
        pass


    
