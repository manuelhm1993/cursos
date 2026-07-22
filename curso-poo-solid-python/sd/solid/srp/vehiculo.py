from tanque_gasolina import TanqueGasolina

class Vehiculo:
    # Para cumplir el SRP: la clase Vehiculo solo debe tener la responsabilida de movimiento
    def __init__(self, tanque: TanqueGasolina) -> None:
        self.__posicion = 0
        self.__tanque   = tanque

    def mover(self, distancia: float) -> None:
        consumo = distancia / 2

        if self.__tanque.get_gasolina() >= consumo:
            self.__posicion += distancia
            self.__tanque.consumir_gasolina(consumo)

            print(f"El vehículo se ha movido {distancia}km. El tanque tiene {self.__tanque.get_gasolina()}lt")
        else:
            print("No hay suficiente gasolina")

    def get_posicion(self) -> str:
        return f"Kilómetros recorridos: {self.__posicion}km"