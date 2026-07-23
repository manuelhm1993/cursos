"""Un decorador es una función que toma otra función como entrada, le agrega un código
adicional, una funcionalidad extra y retorna la función modificada sin alterar el código original
"""
from typing import Callable

# Función decoradora, recibe una función como parámetro. Se usa Callable para indicar el tipo función
def decorador(funcion: Callable) -> Callable:
    # Función para realizar la decoración
    def funcion_modificada() -> None:
        # Código decorador
        print("Antes de llamar a la función")
        # Función original
        funcion()
        # Código decorador
        print("Después de llamar a la función")

    # Se retorna la referencia a la función, no su ejecución, sin paréntesis()
    return funcion_modificada

# Función normal sin decorar
def saludo():
    print("Hola Manuel")

# Decorar la función y guardar el resultado en un objeto Callable
saludo_decorado = decorador(saludo)

# Ejecutar la función decorada
saludo_decorado()