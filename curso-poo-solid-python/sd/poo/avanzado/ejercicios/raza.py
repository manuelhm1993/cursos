from abc import ABC, abstractmethod

class Raza(ABC):
    # ------------------------ Constructor
    def __init__(self, nombre_raza: str, nombre_persona: str, nombre_ataque: str, poder_pelea: float):
        super().__init__()
        self.__nombre_raza    = nombre_raza
        self.__nombre_persona = nombre_persona
        self.__nombre_ataque  = nombre_ataque
        self.__poder_pelea    = poder_pelea

    # ------------------------ Métodos abstractos
    @abstractmethod
    def atacar(self, ataque: str):
        pass

    # ------------------------ Métodos especiales
    def __str__(self) -> str:
        return f"Raza(\"{self.__nombre_raza}\", \"{self.__nombre_persona}\", \"{self.__nombre_ataque}\", {self.__poder_pelea})"

    # ------------------------ Métodos definidores y accesores
    @property
    def nombre_raza(self) -> str:
        return self.__nombre_raza
    
    @nombre_raza.setter
    def nombre_raza(self, nombre: str) -> None:
        self.__nombre_raza = nombre

    @property
    def nombre_persona(self) -> str:
        return self.__nombre_persona
    
    @nombre_persona.setter
    def nombre_persona(self, nombre: str) -> None:
        self.__nombre_persona = nombre

    @property
    def nombre_ataque(self) -> str:
        return self.__nombre_ataque
    
    @nombre_ataque.setter
    def nombre_ataque(self, nombre_ataque: str) -> None:
        self.__nombre_ataque = nombre_ataque

    @property
    def poder_pelea(self) -> float:
        return self.__poder_pelea
    
    @poder_pelea.setter
    def poder_pelea(self, poder_pelea: float) -> None:
        self.__poder_pelea = poder_pelea