# Con la importación en el paquete "paquete.calculos" se puede invocar cada función desde él
# from paquetes.calculos import sumar, restar, multiplicar, dividir, potenciar, redondear

# Para ser más específico se usa de esta manera, pero es lo que suple la importación en un paquete general
from paquetes.calculos.basicos.operaciones import sumar, restar, multiplicar, dividir
from paquetes.calculos.redondeo_potencia.operaciones import potenciar, redondear

dividir(4, 6)
potenciar(4, 6)
redondear(4.8, 2)