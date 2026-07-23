from abc import ABC, abstractmethod

class IDurmiente(ABC):
    @abstractmethod
    def dormir(self) -> None:
        pass