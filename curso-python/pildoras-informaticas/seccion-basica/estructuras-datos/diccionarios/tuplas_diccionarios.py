# Usar tuplas como claves de diccionarios
paises    = ("Venezuela", "Francia", "Reino Unido", "Alemania")
capitales = ("Caracas", "París", "Londres", "Berlín")

# zip() une los elementos índice por índice, y dict() arma el diccionario
dict_paises = dict(zip(paises, capitales))

print(dict_paises)