def sumar(num1: int, num2: int)       -> int: return num1 + num2
def restar(num1: int, num2: int)      -> int: return num1 - num2
def multiplicar(num1: int, num2: int) -> int: return num1 * num2
def dividir(num1: int, num2: int)     -> float: 
    try:
        resultado = num1 / num2
    except ZeroDivisionError as e:
        resultado = "Operación errónea, no se puede dividir por cero"
    
    return resultado

def lookup(operacion: str, num1: int, num2: int) -> int | float | str:
    # Para evitar que todas las funciones se ejecuten al cargar, se guarda una referencia
    operaciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir
    }

    default = f"Operación {operacion} no contemplada"
    funcion_encontrada = operaciones.get(operacion)

    # Si la función es encontrada entonces se ejecuta, si no, se devuelve el default
    return funcion_encontrada(num1, num2) if funcion_encontrada else default

while True:
    try:
        num1 = int(input("Ingrese el operador 1: "))
        num2 = int(input("Ingrese el operador 2: "))
        break
    except ValueError as e:
        print("Error. Ingrese un valor numérico")

operacion = input("Ingrese la operación a realizar (Sumar, Restar, Multiplicar, Dividir): ").lower()

resultado = lookup(operacion, num1, num2)

print(f"{operacion.capitalize()} {num1} y {num2} = {resultado}" if isinstance(resultado, (int, float)) else resultado)
print("Operación ejecutada. Continuación de ejecución del programa.")