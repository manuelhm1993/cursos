import sqlite3
import pandas as pd # Librería para manipulación de datos

from pathlib import Path

# Ruta a la BD original, relativa a este script (sube 2 niveles, baja a resources/databases)
DB_PATH = Path(__file__).parent.parent.parent / "resources" / "databases" / "northwind.db"

square = lambda n: n * n

# Administrador de contexto with
with sqlite3.connect(DB_PATH) as conn:
    conn.create_function("square", 1, square)
    
    cursor = conn.cursor()
    cursor.execute("SELECT *, square(Price) as precio_cuadrado FROM Products WHERE Price > 0")
    
    results = cursor.fetchall()
    results_df = pd.DataFrame(results)

# with cierra automáticamente la conexión y el cursor
print(results_df)