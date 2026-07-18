# Para usar regexp en python se usa el paquete re
import re

# Las expresiones regulares usan patrones para encontrar coincidencias
texto = """Hola maestro, esta es la cadena 1. ¿Cómo estas mi capitán?
Esta es la segunda línea de texto
Y esta es la final definitiva mi capitán"""

# El método search busca en un texto el patrón dado, retorna el primer match o None
resultado = re.search("Hola", texto)

print(resultado)

# El método findall íden search, pero retorna una lista con los match
resultado = re.findall("esta", texto)

print(resultado)

# El parámetro flags permite usar comandos como ignorar mayúsculas y minúsculas
resultado = re.findall("esta", texto, flags=re.IGNORECASE)

print(resultado)