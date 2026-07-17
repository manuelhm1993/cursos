from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df = pd.read_csv(DATOS_CSV_PATH)

# El método head() permite traer desde los encabezados a tantas filas como se indique
primeras_filas = df.head(2)

print(primeras_filas)

# El método tail() ídem head, pero al contrario
ultimas_filas = df.tail(2)

print(ultimas_filas)