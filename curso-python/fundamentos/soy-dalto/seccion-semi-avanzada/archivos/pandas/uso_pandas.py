from ..config.paths import DATOS_CSV_PATH

# Importar pandas, no viene por defecto, así que hay que instalarlo
import pandas as pd

# El reader de pandas devuelve un DataFrame
data_frame = pd.read_csv(DATOS_CSV_PATH)

# Un DataFrame es algo similar a una hoja de cálculo y sirve para análisis de datos
# print(data_frame)

# Mostrando solo la columna nombre
print(data_frame["Nombre"])