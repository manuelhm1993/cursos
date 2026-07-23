# Creando un conjunto con set()
conjunto = set(["Dato1", "Dato2"])

# Ya que los valores de un conjunto son inmutables no permite guardar listas, ni diccionarios
lista       = ["Manuel", "Henriquez", 32]
diccionario = {
    "nombre": "Manuel",
    "apellido": "Henriquez",
    "edad": 32
}

# Si permite guardar tuplas 
tupla = ("Manuel", "Henriquez", 32)

conjunto1 = {tupla}

# Para guardar un conjunto dentro de otro se debe congelar
conjunto1 = frozenset(conjunto1)
conjunto2 = {conjunto1, "Dato2"}

print(conjunto2)