from abc import ABC, abstractmethod

class ITrabajador(ABC):
    @abstractmethod
    def trabajar(self) -> None:
        pass