from carro import Carro
from moto import Moto
from camion import Camion
from vehiculo import desplazamiento_vehiculo

# Listado de objetos vehículo
vehiculos = [Moto(), Carro(), Camion()]

# Polimorfismo y enlazado dinámico y enlazado dinámico
for vehiculo in vehiculos:
    desplazamiento_vehiculo(vehiculo)