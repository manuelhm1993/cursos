from modulos.clases.vehiculo import Vehiculo
from pathlib import Path

import pickle

DATA_CARROS_PATH = Path(__file__).parent / "resources" / "data_carros"

mis_carros = [
    Vehiculo("Mitsubishi", "Lanzer"),
    Vehiculo("Seat", "Leon"),
    Vehiculo("Renault", "Megane")
]

def serializar(path, data):
    with open(path, "wb") as archivo_pickle:
        pickle.dump(data, archivo_pickle)

        print("Datos guardados correctamente")

def deserializar(path):
    with open(path, "rb") as archivo_pickle:
        data = pickle.load(archivo_pickle)
    
    return data

serializar(DATA_CARROS_PATH, mis_carros)

vehiculos = deserializar(DATA_CARROS_PATH)

for vehiculo in vehiculos:
    print(vehiculo.estado(), end="\n\n")
