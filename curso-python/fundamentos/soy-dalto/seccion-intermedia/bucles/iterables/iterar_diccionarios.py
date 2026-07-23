diccionario = {
    "nombre": "Manuel",
    "apellido": "Henriquez",
    "edad": 32
}

# Iterar diccionario por sus claves
for key in diccionario.keys():
    print(diccionario[key])
else:
    print()

# Iterar diccionario por sus valores
for value in diccionario.values():
    print(value)
else:
    print()

# Ídem enumerable
for clave, valor in diccionario.items():
    # Escapar las llaves en un f-string
    print(f"Ítem: {{{clave}:{valor}}}")