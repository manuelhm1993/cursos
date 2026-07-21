# Forma de crear clases abstractas e interfaces en Python
from abc import ABC, abstractmethod

# Esto equivale en Java a public abstract class Persona {}
class Persona(ABC):
    def __init__(self, nombre: str, edad: int, sexo: str, actividad: str) -> None:
        super().__init__()
        self.__nombre    = nombre
        self.__edad      = edad
        self.__sexo      = sexo
        self.__actividad = actividad

    # Definir un método abstracto
    @abstractmethod
    def hacer_actividad(self) -> None:
        pass

    @property
    def actividad(self) -> str:
        return self.__actividad
    
    @actividad.setter
    def actividad(self, actividad: str) -> None:
        self.__actividad = actividad

    def presentarse(self) -> None:
        print(f"Hola, me llamo: {self.__nombre} y tengo {self.__edad} años")