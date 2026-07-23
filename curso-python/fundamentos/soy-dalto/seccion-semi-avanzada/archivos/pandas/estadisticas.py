from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df = pd.read_csv(DATOS_CSV_PATH)

# Obtener datos estadísticos del DataFrame
df_info = df.describe()

print(df_info)