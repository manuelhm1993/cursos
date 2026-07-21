from typing import Callable

# Se importa la clase Callale para definir el tipo de objeto a recibir
def funcion_decoradora(funcion_parametro: Callable) -> Callable:
    # Se define la función que decora
    def funcion_interior() -> Callable:
        print("Resultado: ", end="")
        # Se ejecuta la función
        resultado = funcion_parametro()
        print("Fin del programa", end="\n\n")

        return resultado
    
    # Se retorna una referencia a la función, no su llamada
    return funcion_interior

# Se llama al decorador por la propiedad o etiqueta @
@funcion_decoradora
def sumar() -> None:
    print(15 + 20)

@funcion_decoradora
def restar() -> None:
    print(30 - 10)

sumar()
restar()