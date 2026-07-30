from vehiculo import Vehiculo

class Furgoneta(Vehiculo):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo)
        self.__cargado = False

    def carga(self, cargar: bool) -> str:
        self.__cargado = cargar

        return "La furgoneta está cargada" if self.__cargado else "La furgoneta no está cargada"