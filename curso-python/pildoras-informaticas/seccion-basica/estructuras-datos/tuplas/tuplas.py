# Las tuplas son listas inmutables, es decir, no append, extend, remove...
tupla = ("Manuel", 23, 7, 1993, 23)

# Convertir una tupla en lista
lista       = list(tupla)

# Convertir una lista en tupla
nueva_tupla = tuple(lista)

# Las particiones devuelven otras tuplas, una tupla de un único elemento es ("item",)
print(tupla[:1])

# Imprimir elementos
print(lista)
print(nueva_tupla)

# Comprobar si existe un elemento en la tupla
print("Manuel" in nueva_tupla)

# Contar coincidencias de un elemento
print(f"El número 13 se repite {nueva_tupla.count(23)} en la tupla")

# Método len para saber la cantidad de elementos de la lista
print(f"Cantidad de elementos de la tupla: {len(nueva_tupla)}")