# Para usar regexp en python se usa el paquete re
import re

# Las expresiones regulares usan patrones para encontrar coincidencias
texto = """Hola maestro, esta es la cadena 1. ¿Cómo estas mi capitán?
Esta es la línea 2 de texto. El 256 es un motivo de memes de informática
Y esta es la final (línea 3) definitiva mi capitán."""

r"""Grupos y rangos:
- {n}   -> Buscar 'n' cantidad de veces el valor de la izquierda
- {n,m} -> Buscar 'n' cantidad de veces el valor de la izquierda como mínimo y 'm' como máximo 
- |     -> Es el equivalente al operador 'o'
"""

r"""Conjuntos:
- () -> Coincidir con el patrón interno y se puede aplicar un grupo o rango
- [] -> Coincidir con el patrón interno y sus variantes y se puede aplicar un grupo o rango
"""

# Para construir patrones se usa 'r' delante de las aparturas de las cadenas raw string
pattern = r"\d{1,4}|Hola"

resultado = re.findall(pattern, texto)

print(resultado)
