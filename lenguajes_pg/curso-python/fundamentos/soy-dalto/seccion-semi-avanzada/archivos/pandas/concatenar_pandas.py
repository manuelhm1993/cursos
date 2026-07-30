from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df1 = pd.read_csv(DATOS_CSV_PATH)
df2 = pd.read_csv(DATOS_CSV_PATH)

# Concatenando los dos df
df_concatenado = pd.concat([df1, df2])

print(df_concatenado)