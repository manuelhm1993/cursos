# Guardar la ruta del archivo
path_relativa = "archivos\\resources\\archivo.txt"

# Abrir el archivo y almacenarlo en una variable, se le pasa el path y la codificación
archivo = open(path_relativa, encoding="UTF-8")

# Leer y guardar el contenido del archivo en una lista con cada línea
lista = archivo.readlines()

# Cerrar el archivo
archivo.close()

# Mostrar la lista
print(lista)