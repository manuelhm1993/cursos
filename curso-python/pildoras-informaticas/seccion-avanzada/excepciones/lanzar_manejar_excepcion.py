from math import sqrt

def calcular_raiz_cuadrada(numero: int) -> None:
    if numero < 0:
        raise ValueError("No se puede hallar la raíz cuadrada de un número negativo")
    else:
        print(f"La raíz cuadrada de {numero} es {sqrt(numero)}")

numero = int(input("Ingrese un número: "))

try:
    calcular_raiz_cuadrada(numero)    
except ValueError as e:
    print(e)

print("Fin del programa.")