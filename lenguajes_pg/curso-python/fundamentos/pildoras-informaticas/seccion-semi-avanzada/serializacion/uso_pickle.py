""" El guardado permanente binario con pickle está desaconsejado hoy en dia, solo se usa
en proyectos antigüos o entrenamientos de IA, actualmente se recomienda json"""
from pathlib import Path

import pickle

DATA_NOMBRES_PATH = Path(__file__).parent / "resources" / "data_nombres"

nombres = ["Manuel", "Sugey", "Carlos", "Ender"]

def crear_archivo_binario():
    # Crear un archivo binario de una lista de nombres
    with open(DATA_NOMBRES_PATH, "wb") as archivo:
        pickle.dump(nombres, archivo)

        print("Archivo serializado correctamente")

def leer_archivo_binario():
    # Leer un archivo binario
    with open(DATA_NOMBRES_PATH, "rb") as archivo:
        data = pickle.load(archivo)

    return data

print(leer_archivo_binario())