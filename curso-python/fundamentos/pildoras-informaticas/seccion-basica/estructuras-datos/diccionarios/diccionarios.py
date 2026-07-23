# Crear un diccionario clave:valor, es prácticamente un json
diccionario = {
    "Alemania": "Berlín",
    "Francia": "París",
    "Reino Unido": "Londres",
    "Venezuela": "Caracas"
}

# Agregar un nuevo elemento al diccionario
diccionario["Italia"] = "Lisboa"

# Imprimir el diccionario
print(diccionario)

# Acceder a un valor por su clave
print(f"La capital de Venezuela es {diccionario['Venezuela']}")

# Modificar un elemento del diccionario
diccionario["Italia"] = "Roma"

print(diccionario)

# Eliminar un elemento del diccionario
del diccionario["Italia"]

print(diccionario)