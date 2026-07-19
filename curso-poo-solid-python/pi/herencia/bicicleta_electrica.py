from vehiculo import Vehiculo
from vehiculo_electrico import VehiculoElectrico

# En la herencia múltiple se prioriza el orden MRO: Method Resolution Order Left -> Right
class BicicletaElectrica(VehiculoElectrico, Vehiculo):
    # Para usar ambos constructores y eliminar MRO, no se debe usar super, si no una llamada explícita a la clase, init y self
    def __init__(self, marca: str, modelo: str):
        VehiculoElectrico.__init__(self)
        Vehiculo.__init__(self, marca, modelo)