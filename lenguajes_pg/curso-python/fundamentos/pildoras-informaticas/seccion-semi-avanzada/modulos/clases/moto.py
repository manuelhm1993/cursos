# Importación relativa para que busque a partir de este directorio
from .vehiculo import Vehiculo

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__hacer_caballito = ""

    def caballito(self):
        self.__hacer_caballito = "- Voy haciendo el caballito"
    
    def estado(self):
        return f"{super().estado()} {"\n" + self.__hacer_caballito if self.__hacer_caballito else ""}"