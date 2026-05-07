from abc import ABC, abstractmethod
import numpy as np


class Kinematics(ABC):
    @abstractmethod
    def IK(self, v: np.ndarray) -> np.ndarray:
        ...

    @abstractmethod
    def FK(self, thetas: np.ndarray) -> np.ndarray:
        ...
