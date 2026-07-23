# from clases import (furgoneta, moto, vehiculo_electrico)

from clases.vehiculo import Vehiculo
from clases.furgoneta import Furgoneta
from clases.moto import Moto
from clases.vehiculo_electrico import VehiculoElectrico

mi_carro = Vehiculo("Mitsubishi", "Lanzer")

print(mi_carro.estado())