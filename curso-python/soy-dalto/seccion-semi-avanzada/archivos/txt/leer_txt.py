from pathlib import Path

# Usar el objeto Path para obtener rutas absolutas de forma automatizada
FIELD_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

# Abrir el archivo y almacenarlo en una variable, se le pasa el path y la codificación
archivo = open(FIELD_PATH, encoding="UTF-8")

# Leer y guardar el contenido del archivo
contenido = archivo.read()

# Cerrar el archivo
archivo.close()

# Mostrar el contenido
print(contenido)