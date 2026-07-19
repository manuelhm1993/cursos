import re

# Detectar un número CABA y ocultarlo
texto = "Hola Sugey, mi número es: +58 424-6827377"

pattern = r"\+\d{2}\s\d{3}-\d{7}"

texto = re.sub(pattern, "(Número oculto)", texto)

print(texto)