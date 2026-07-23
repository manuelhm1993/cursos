import re

texto = "Vamos a aprender expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla."

pattern = "Python"

# Encuentra todas las coincidencias en un texto y devuelve una lista
resultado = re.findall(pattern, texto)

print(f"La palabra {pattern} se encuentra {len(resultado)} veces en el texto")