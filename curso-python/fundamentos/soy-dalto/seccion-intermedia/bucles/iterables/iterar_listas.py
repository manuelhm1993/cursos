lista = ["Gato", "Perro", "Loro", "Cocodrilo"]

# Obtener el rango de iteración
n_items = range(len(lista))

# No es la forma más óptima
for i in n_items:
    print(lista[i])
else:
    print()

# Recorrido optimizado, enumerate devuelve un iterable con el índice y el valor
for indice, valor in enumerate(lista):
    print(f"Ítem [{indice}:{valor}]")

