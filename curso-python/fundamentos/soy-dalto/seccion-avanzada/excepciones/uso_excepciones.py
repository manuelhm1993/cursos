"""Las excepciones son eventos de tipo error que interrumpen el flujo de ejecución
y finalizan el programa, aprender a manejarlas implica indicarle al código qué hacer
cuando ocurren"""
def sumar():
    # Bucle infinito para manejar la posible excepción
    while True:
        # Si el try se ejecuta, se rompe el bucle con else
        try:
            a = int(input("Ingrese el operador 1: "))
            b = int(input("Ingrese el operador 2: "))

            resultado = a + b
        
        # Si except se ejecuta vuelve a solicitar los datos
        except ValueError as e:
            print("Te pedí un número salame, no te hagas el gracioso")
            print(f"Error: {e}")
        # Se puede usar else en cualquier sentencia
        else:
            break
        # Esto se ejecuta siempre
        finally:
            print("Esto se ejecuta siempre")

    return resultado

print(sumar())