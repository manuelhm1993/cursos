from abc import ABC, abstractmethod

class IComedor(ABC):
    @abstractmethod
    def comer(self) -> None:
        pass