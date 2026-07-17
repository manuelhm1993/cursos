from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df = pd.read_csv(DATOS_CSV_PATH)

# Obtener la cantidad de filas y columnas del DataFrame en una tupla
filas, columnas = df.shape

print(f"La cantidad de filas es {filas} y la cantidad de columnas es {columnas}")