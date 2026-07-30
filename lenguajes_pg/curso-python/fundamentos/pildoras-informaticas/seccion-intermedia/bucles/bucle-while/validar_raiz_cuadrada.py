# Importar todo el paquete
# import math

# Importar una función específica
from math import sqrt

print("Programa de cálculo de raíz cuadrada: ")

numero = float(input("Ingrese un número: "))
intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos. Programa finalizado")
        break

    numero = float(input("Ingrese un número: "))

    if numero < 0:
        intentos += 1

if intentos < 2:
    print(f"La raíz cuadrada de {numero} es {sqrt(numero)}")