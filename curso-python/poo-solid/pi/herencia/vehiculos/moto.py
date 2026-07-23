# Importar del módulo vehiculo la clase Vehiculo
from vehiculo import Vehiculo

# Heredar de la clase vehículo
class Moto(Vehiculo):
    def __init__(self, marca: str, modelo: str):
        # Llamar al constructor de la clase padre
        super().__init__(marca, modelo)

        self.__caballito = "No todavía"

    def caballito(self) -> None:
        self.__caballito = "Voy haciendo el caballito"

    # Sobreescritura de un método
    def estado(self):
        super().estado()
        print(f"- Caballito:  {self.__caballito}")