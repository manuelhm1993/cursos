lista = ["Manuel Henriquez", "MHenriquez", True, 1.70]
tupla = ("Manuel Henriquez", "MHenriquez", True, 1.70)

lista[3] = "Sugey Godoy"

""" Conjunto de datos set: son elementos desordenados y son inmutables, similares a las tuplas, pero no 
permite datos duplicados, los agrupa y tampoco se puede acceder por índices, solo se puede acceder iterando"""
conjunto = {"Manuel Henriquez", "MHenriquez", True, 1.70}

diccionario = {
    "nombre": "Manuel Henriquez",
    "usuario": "MHenriquez",
    "es_programador": True,
    "altura": 1.70
}

print(diccionario["nombre"])