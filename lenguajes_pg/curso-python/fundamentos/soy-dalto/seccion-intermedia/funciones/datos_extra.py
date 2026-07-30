# Función con parámetro opcional (los parámetros opcionales van luego de los obligatorios)
def frase(nombre, apellido, adjetivo = "tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

# Forzar el orden de los argumentos: keyword params
frase_resultante = frase(adjetivo="inteligente", nombre="Manuel", apellido="Henriquez")

print(frase_resultante)