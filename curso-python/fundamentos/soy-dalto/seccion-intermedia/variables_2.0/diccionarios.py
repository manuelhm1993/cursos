# Creando diccionarios con la función dict
diccionario = dict(nombre="Manuel", apellido="Henriquez")

print(diccionario)

# Crear diccionarios con fromkeys, permite crear diccionarios con valores nulos
diccionario = dict.fromkeys(("nombre", "apellido", "edad"), None)

print(diccionario)