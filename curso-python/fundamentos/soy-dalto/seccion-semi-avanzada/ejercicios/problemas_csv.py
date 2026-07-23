from pathlib import Path

import pandas as pd

PROBLEMAS_CSV_PATH = Path(__file__).parent / "resources" / "problemas_csv.csv"

df = pd.read_csv(PROBLEMAS_CSV_PATH)

# 1. Convertir la edad de int a string los datos de una columna
df["Edad"] = df["Edad"].astype(str)

print(type(df.loc[:, "Edad"][0]))

# 2. Reemplazar valores
df["Apellido"] = df["Apellido"].replace("Henriquez", "CEO")

print(df.loc[0, "Apellido"])

# 3. Eliminar datos faltantes
print(df)

df = df.dropna()

print(df)

# 4. Eliminar datos duplicados
df = df.drop_duplicates()

print(df)

# 5. Crear un csv con el df resultado
df.to_csv(Path(__file__).parent / "resources" / "datos_depurados.csv")