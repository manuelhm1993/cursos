from collections.abc import Generator # Declarar un generador explícitamente
from collections.abc import Iterator  # Íden Generator, pero si no tiene return ni send

# ----------------------- Devolver pares con funciones ----------------------- #
def devolver_pares_for(cantidad: int) -> list[int]:
    lista_pares: list[int] = []

    for i in range(1, (cantidad + 1)):
        lista_pares.append(i * 2)

    return lista_pares

def devolver_pares_while(cantidad: int) -> list[int]:
    lista_pares: list[int] = []
    i = 1

    while i <= cantidad:
        lista_pares.append(i * 2)
        i += 1

    return lista_pares

def devolver_pares_map(cantidad: int) -> list[int]:
    return [*map(lambda n: n * 2, [*range(1, (cantidad + 1))])]

# ---------------------- Devolver pares con generadores ---------------------- #
def devolver_pares_for_yield(cantidad: int) -> Iterator[int]:
    for i in range(1, cantidad + 1):
        yield i * 2

def devolver_pares_while_yield(cantidad: int) -> Generator[int, None, None]:
    i = 1

    while i <= cantidad:
        # Lazy loader: devolver un iterable con cada valor
        yield i * 2

        i += 1

# ----------------- 1. Usando Expresión Generadora ----------------- #
def devolver_pares_expresion(cantidad: int) -> Generator[int, None, None]:
    """
    Forma más 'Pythonica' y rápida para lógica simple.
    Fíjate que retorna el generador directamente sin usar la palabra 'yield'.
    """
    return (n * 2 for n in range(1, cantidad + 1))


# ----------------- 2. Usando yield from con map ----------------- #
def devolver_pares_yield_from(cantidad: int) -> Generator[int, None, None]:
    """
    Delega la generación de valores a map().
    Evita tener que escribir:
    for n in map(lambda x: x * 2, range(1, cantidad + 1)):
        yield n
    """
    yield from map(lambda n: n * 2, range(1, cantidad + 1))

# --------------------------- Llamadas a funciones --------------------------- #
print(devolver_pares_for(10))
print(devolver_pares_while(10))
print(devolver_pares_map(10))

# -------------------------- Llamadas a generadores -------------------------- #
# Instanciamos la máquina (no se ejecuta nada todavía)
generador = devolver_pares_expresion(10)

# Le pedimos valores a la máquina manualmente
print(next(generador))
print("--- Hacemos otra cosa en el código, el generador sigue pausado ---")
print(next(generador))
print(next(generador))