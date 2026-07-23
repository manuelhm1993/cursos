from datetime import date

def calcular_edad(anio_nacimiento: int) -> tuple:
    anio_actual     = date.today().year
    edad = anio_actual - anio_nacimiento

    return (anio_actual, edad)

def evaluar_edad() -> None:
    anio_nacimiento   = int(input("Ingrese su año de nacimiento: "))

    # Lanzar una excepción intencionalmente si se cumple una condición
    if anio_nacimiento < 0:
        raise ValueError("No se permiten años negativos")

    anio_actual, edad = calcular_edad(anio_nacimiento)

    if edad < 20:
        mensaje = "Eres muy joven"
    elif edad < 40:
        mensaje = "Eres joven"
    elif edad < 65:
        mensaje = "Eres maduro"
    elif edad < 100:
        mensaje = "Debes cuidarte"
    
    print(f"Usted nació en {anio_nacimiento} este año {anio_actual} cumple: {edad} años. {mensaje}.")

evaluar_edad()