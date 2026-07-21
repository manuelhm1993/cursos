from typing import Callable

def funcion_decoradora(funcion_parametro: Callable) -> Callable:
    # *args captura todos los argumentos posicionales y arma una tupla **kwargs ídem *args, pero captura los nombrados y arma un dict
    def funcion_interior(*args, **kwargs) -> Callable:
        print("Resultado: ", end="")
        # Se ejecuta la función pasándole los argumentos capturados en funcion_interior
        resultado = funcion_parametro(*args, **kwargs)
        print("Fin del programa", end="\n\n")

        return resultado
    
    # Se retorna una referencia a la función, no su llamada
    return funcion_interior

# Se llama al decorador por la propiedad o etiqueta @
@funcion_decoradora
def sumar(num1: float, num2: float, num3: float) -> None:
    print(num1 + num2 + num3)

@funcion_decoradora
def restar(num1: float, num2: float) -> None:
    print(num1 - num2)

@funcion_decoradora
def potencia(base: float, exponente: float) -> None:
    print(pow(base, exponente))

sumar(7, 5, 8)
restar(12, 10)
potencia(base=5, exponente=3)