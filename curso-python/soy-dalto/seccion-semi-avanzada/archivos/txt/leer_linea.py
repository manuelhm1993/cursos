# Guardar la ruta del archivo
path_relativa = "archivos\\resources\\archivo.txt"

# Abrir el archivo y almacenarlo en una variable, se le pasa el path y la codificación
archivo = open(path_relativa, encoding="UTF-8")

# Leer y guardar el contenido de la primera línea del archivo
linea1 = archivo.readline()

# Cerrar el archivo
archivo.close()

# Mostrar La línea 1
print(linea1)