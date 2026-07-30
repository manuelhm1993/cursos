"""SRP: Principio de responsabilidad única, dicta que una clase debe tener una y
solo una razón para cambiar, es decir, una sola responsablidad o tarea."""
from vehiculo import Vehiculo
from tanque_gasolina import TanqueGasolina

tanque   = TanqueGasolina(100)
vehiculo = Vehiculo(tanque)

lista_movimientos: list[int] = [10, 20, 60, 100, 100]

print(vehiculo.get_posicion(), end="\n\n")

for movimiento in lista_movimientos:
    vehiculo.mover(movimiento)
    print(vehiculo.get_posicion(), end="\n\n")
