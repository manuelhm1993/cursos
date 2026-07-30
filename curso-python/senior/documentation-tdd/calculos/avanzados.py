from math import sqrt

def raiz_cuadrada(numeros: list[int]) -> list[float]:
    r"""Calcular la raíz cuadrada de una lista de números y devolver una nueva lista
    con los nuevos valores. Se usan expresiones anidadas en estas TDD

    Args:
        numeros (list[int | float]): lista de números

    Returns: 
        list[float]: una lista con los resultados de la raíz cuadrada de los números originales

    Raises:
        ValueError: si se pasa un número negativo, no se puede calcular su raíz

    Example:
        >>> raiz_cuadrada([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144])
        [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]

        >>> lista = []
        >>> for i in [4, 9, 16]:
        ...     lista.append(i)
        >>> raiz_cuadrada(lista)
        [2.0, 3.0, 4.0]

        >>> lista = []
        >>> for i in [4, -9, 16]:
        ...     lista.append(i)
        >>> raiz_cuadrada(lista)
        Traceback (most recent call last):
            ...
        ValueError: expected a nonnegative input, got -9.0
    """

    # Para el escape de el caracter '\' se usa \\, pero en rutas largas es complejo, así que se usa rawstring r"\"
    # Los ... indican expresiones anidadas y permiten controlar los errores

    # Compresión de listas
    return [sqrt(n) for n in numeros]