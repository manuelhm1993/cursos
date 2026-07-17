""" El guardado permanente con JSON es el estándar actual de la industria.
Es seguro, legible por humanos y compatible con cualquier lenguaje (Frontend, Laravel, etc). """
from pathlib import Path

import json

DATA_NOMBRES_PATH = Path(__file__).parent / "resources" / "data_nombres.json"

nombres = ["Manuel", "Sugey", "Carlos", "Ender"]

def crear_archivo_json():
    with open(DATA_NOMBRES_PATH, "w", encoding="utf-8") as archivo:
        json.dump(nombres, archivo, indent=4)

        print("Archivo JSON serializado y guardado correctamente")

def leer_archivo_json():
    with open(DATA_NOMBRES_PATH, "r", encoding="utf-8") as archivo:
        data = json.load(archivo)

    return data

crear_archivo_json()
print(leer_archivo_json())