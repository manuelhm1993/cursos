# Importación relativa para que busque a partir de este directorio
from .vehiculo import Vehiculo

class VehiculoElectrico(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)

        self.__autonomia = 100
        self.__cargando = False

    def cargar_energia(self):
        self.__cargando = True

    def estado(self):
        return f"{super().estado()} \n- Cargando: {self.__cargando}"