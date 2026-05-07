from abc import abstractmethod,ABC

class Body(ABC):
    def __init__(self) -> None:
        pass


    @abstractmethod
    def update(self):
        pass
