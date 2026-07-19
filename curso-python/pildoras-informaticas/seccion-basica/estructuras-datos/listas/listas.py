# Las listas son estructuras de datos equivalentes a los arrays, pero más potentes en python
lista  = ["Fernando", "Ender", "Sugey"]
manuel = ["Manuel", 32, True, 1.70]

# Agregar un elemento al final de la lista
lista.append("Sugey")

# Agregar un elemento en una posición específica de la lista
lista.insert(2, "Carlos")

# Agregar varios elementos al final de la lista
lista.extend(manuel)

# Eliminar un elemento de la lsita
lista.remove("Sugey")

# Eliminar el último elemento de la lista
print(lista.pop())

# Imprimir el índice de un elemento de la lista
print(lista.index("Sugey"))

# Validar si un elemento está en la lsita
print("Sugey" in lista)

# Imprimir todos los elementos de la lista
print(lista[:])