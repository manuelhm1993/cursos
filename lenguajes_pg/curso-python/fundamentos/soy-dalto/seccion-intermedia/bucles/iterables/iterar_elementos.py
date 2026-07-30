# Crear dos estructuras. Las iteraciones son iguales para cualquier estructura: lista, tupla, conjunto
animales = {"Gato", "Perro", "Loro", "Cocodrilo"}
numeros  = (52, 16, 14, 72)
i = 0

# La función zip devuelve una tupla con los elementos de ambas estructuras
for numero, animal in zip(numeros, animales):
    i += 1

    print(f"Iteración {i} conjunto Número: {numero}")
    print(f"Iteración {i} tupla Animal: {animal}")
