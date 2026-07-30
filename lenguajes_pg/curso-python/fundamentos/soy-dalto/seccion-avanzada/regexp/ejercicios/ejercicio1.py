# Crear un patrón que busque un número seguido de un punto y un espacio
import re

texto = """Hola maestro, esta es la cadena 1. ¿Cómo estas mi capitán?
Esta es la línea 2 de texto
Y esta es la final (línea 3) definitiva mi capitán."""

patron = r"\d\.\s"

resultado = re.findall(patron, texto)

print(resultado)