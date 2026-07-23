# Iterar sobre dos listas en paralelo, deben tener la misma cantidad de elementos
animales = ["Gato", "Perro", "Loro", "Cocodrilo"]
numeros  = [52, 16, 14, 72]
i = 0

# La función zip devuelve una tupla con los elementos de ambas tuplas 
for numero, animal in zip(numeros, animales):
    i += 1

    print(f"Iteración {i} lista #1. Número: {numero}")
    print(f"Iteración {i} lista #2. Animal: {animal}")
