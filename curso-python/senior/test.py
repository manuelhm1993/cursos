import re

seccion = "moñongo"

seccion = re.sub(r"[áéíóúÁÉÍÓÚñÑäëïöüÄËÏÖÜ]", "_", seccion).capitalize()

print(seccion)