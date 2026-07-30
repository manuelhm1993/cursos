from ..config.paths import DATOS_CSV_PATH

# Librería estándar de csv para manipular archivos
import csv

with open(DATOS_CSV_PATH, "r", encoding="UTF-8") as archivo:
    # Objeto reader, es un iterable
    reader = csv.reader(archivo)

    # Iterar el objeto fila a fila
    for row in reader:
        # Cada fila es una lista con los items correspondientes
        print(row)