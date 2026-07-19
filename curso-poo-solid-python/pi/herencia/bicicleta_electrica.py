from vehiculo import Vehiculo
from vehiculo_electrico import VehiculoElectrico

# En la herencia múltiple se prioriza el orden a la hora de llamar a los constructores
class BicicletaElectrica(VehiculoElectrico, Vehiculo):
    pass