from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df = pd.read_csv(DATOS_CSV_PATH)

# Ordenar por edad ascendente. Retorna un nuevo objeto, no ordena el actual
df_ordenado = df.sort_values("Edad")

print(df_ordenado, end="\n\n")

# Ordenado descendente
df_ordenado = df.sort_values("Edad", ascending=False)

print(df_ordenado)