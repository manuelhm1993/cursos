# Situar el puntero en medio del archivo de texto
from os import SEEK_END
from pathlib import Path

FIELD_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

def forma_archivos(archivo):
    archivo.seek(0, SEEK_END)

    longitud_archivo = archivo.tell()
    mitad_archivo = int(longitud_archivo / 2) if longitud_archivo % 2 == 0 else round(longitud_archivo / 2)

    archivo.seek(mitad_archivo)

    contenido = archivo.read()

    print(contenido)

def forma_texto(archivo):
    contenido = archivo.read()

    longitud_archivo = len(contenido)
    mitad_archivo = int(longitud_archivo / 2) if longitud_archivo % 2 == 0 else round(longitud_archivo / 2)
    
    archivo.seek(mitad_archivo)

    contenido = archivo.read()

    print(contenido)

with open(FIELD_PATH, "r", encoding="UTF-8") as archivo:
    forma_texto(archivo)
