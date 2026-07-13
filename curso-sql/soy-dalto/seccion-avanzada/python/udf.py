import sqlite3
import pandas as pd # Librería para manipulación de datos

from pathlib import Path

# Ruta a la BD original, relativa a este script (sube 2 niveles, baja a resources/databases)
DB_PATH = Path(__file__).parent.parent.parent / "resources" / "databases" / "northwind.db"

square = lambda n: n * n

conn = sqlite3.connect(DB_PATH)

# Crear una UDF: nombre, número de argumentos, función python
conn.create_function("square", 1, square)

# Crear un cursor para ejecutar consultas
cursor = conn.cursor()
cursor.execute(
    """
    SELECT * FROM Products
    """
)

result = cursor.fetchall()
result_df = pd.DataFrame(result)

# Confirmar los cambios en la db, aunque en este caso no es necesario
conn.commit()

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

print(result_df)