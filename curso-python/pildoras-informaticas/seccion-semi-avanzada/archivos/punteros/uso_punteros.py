from pathlib import Path
from os import SEEK_END

FIELD_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

with open(FIELD_PATH, "r", encoding="UTF-8") as archivo:
    # Llevar el puntero al final del archivo
    archivo.seek(0, SEEK_END)

    # Saber la longitud del archivo
    longitud = archivo.tell()

    # Llevar el puntero al inicio del archivo
    archivo.seek(0)

    # El puntero es un equivalente del cursor un un procesador de texto
    print(archivo.read())

    if archivo.tell() == longitud:
        archivo.seek(0)

    # Al posicionar con seek en la primera posición, permite leer nuevamente el archivo
    print(archivo.read())

