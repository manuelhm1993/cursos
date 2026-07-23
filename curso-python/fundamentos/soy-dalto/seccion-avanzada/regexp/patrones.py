# Para usar regexp en python se usa el paquete re
import re

# Las expresiones regulares usan patrones para encontrar coincidencias
texto = """Hola maestro, esta es la cadena 1. ¿Cómo estas mi capitán?
Esta es la línea 2 de texto
Y esta es la final (línea 3) definitiva mi capitán."""

r"""Patrones:
- \d -> Busca valores numéricos entre 0 y 9:                                 [0-9]
- \D -> Busca todo menos valores numéricos entre 0 y 9:                      [^0-9]
- \w -> Busca valores alfanuméricos incluyendo '_':                          [a-zA-Z0-9_]
- \W -> Busca todo menos valores alfanuméricos incluyendo '_':               [^a-zA-Z0-9_]
- \s -> Busca espacios en blanco, tabs y saltos en línea:                    [\f\n\r\t\v ]
- \S -> Busca todo menos espacios en blanco, tabs y saltos en línea:         [^\f\n\r\t\v ]
- .  -> Busca todo menos saltos en línea:                                    [^\n]
- \n -> Busca saltos en línea                                                
- \  -> Cancelar caracteres especiales, sirve para escapar caractes como '.' 
- ^  -> Dentro de un rango significa negar, al inicio significa comienzo con
- $  -> Terminar con
"""

# Para construir patrones se usa 'r' delante de las aparturas de las cadenas raw string
pattern = r"texto$"

# El flag re.M indica multilinea, que significa que cada línea nueva es un comienzo de cadena
resultado = re.findall(pattern, texto, flags=re.M)

print(resultado)
