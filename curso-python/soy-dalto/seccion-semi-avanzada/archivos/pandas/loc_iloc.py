from ..config.paths import DATOS_CSV_PATH

import pandas as pd

df = pd.read_csv(DATOS_CSV_PATH)

# Acceder a un elemento específico del df con loc, se puede indicar la columna
elemento = df.loc[2, "Edad"]

print(elemento)

# Acceder a un elemento específico del df por su índice iloc, si no se indica segundo parámetro, devuelve todo
elemento = df.iloc[2, 2]

print(elemento)

# Accediendo a todas las filas de una columna
# apellidos = df["Apellido"]

# Al hacer slicing de dos dimensiones la ',' indica el corte de eje todas las filas y solo la columna 1
apellidos = df.iloc[:,1]

print(apellidos)

# Accediendo a la fila 3 con loc
edades = df.loc[:,"Nombre"]

print(edades)

# Condicionales, filas con edad mayor a 30
mediana_edad = df.loc[df["Edad"] > 30, :]

print(mediana_edad)