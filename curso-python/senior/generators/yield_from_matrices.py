# El parámetro *args permite un número indeterminado de elementos y los empaqueta en una tupla
def devolver_ciudades(*ciudades):
    for ciudad in ciudades:
        # for caracter in ciudad:
        #     yield caracter
        #
        # Simplifica la sintaxis de un bucle anidado
        yield from ciudad

lista_ciudades: list[str] = [
    "Caracas", "Maracaibo", "Mérida", "Margarita"
]

# También el '*' sirve para desempaquetar un iterable
generador = devolver_ciudades(*lista_ciudades)

print(next(generador))
print(next(generador))