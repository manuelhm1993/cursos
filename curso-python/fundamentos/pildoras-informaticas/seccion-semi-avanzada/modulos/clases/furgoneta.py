# Importación relativa para que busque a partir de este directorio
from .vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.__cargado = cargar

        respuesta = ""

        if self.__cargado:
            respuesta = "La furgonera está cargada"
        else:
            respuesta = "La furgonera no está cargada"
        
        return respuesta