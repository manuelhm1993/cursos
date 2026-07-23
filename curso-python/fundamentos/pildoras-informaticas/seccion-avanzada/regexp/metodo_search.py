import re

texto = "Vamos a aprender expresiones regulares"

pattern = "aprender"

print("Texto encontrado" if re.search(pattern, texto) is not None else "Texto no encontrado")