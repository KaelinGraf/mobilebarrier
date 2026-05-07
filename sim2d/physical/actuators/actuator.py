from abc import ABC, abstractmethod
import numpy as np


class Actuator(ABC):

    @abstractmethod
    def command(self, u: np.ndarray) -> None:
        ...

    @abstractmethod
    def integrate(self, dt: float) -> None:
        ...
