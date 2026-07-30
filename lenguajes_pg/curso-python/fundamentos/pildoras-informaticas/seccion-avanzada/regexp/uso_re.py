import re

texto = "Vamos a aprender expresiones regulares"

pattern = "aprender"

# Devuelve un objeto con la coincidencia y el span de índices o None si hay match
resultado = re.search(pattern, texto)

# Devuelve el índice donde inicia la coincidencia
print(f"La coincidencia inicia en el índice: {resultado.start()}")

# Devuelve el finaliza donde inicia la coincidencia
print(f"La coincidencia finaliza en el índice: {resultado.end()}")

# Devuelve una tupla con los índices de inicio y fin de la coincidencia
print(f"La coincidencia se ubica en los índices: {resultado.span()}")