import re

def funcion_match(pattern: str, texto: str) -> None:
    # El método match busca coincidencias del patrón en el inicio del texto
    if re.match(pattern, texto):
        print("Coincide")
    else:
        print("No coincide")

def funcion_search(pattern: str, texto: str) -> None:
    # El método search busca coincidencias del patrón en todo el texto
    if re.search(pattern, texto, flags=re.IGNORECASE):
        print("Coincide")
    else:
        print("No coincide")

nombre1 = "Lara López"
nombre2 = "Jara Gómez"
nombre3 = "María LÓpez"

pattern = r"L[oó]pez"

funcion_search(pattern, nombre3)