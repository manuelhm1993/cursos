""" Crear un programa que muestre la rentabilidad de los empleados y los productos.
Se deben mostrar los gráficos para ver dichas rentabilidades
"""
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

DB_PATH = Path(__file__).parent.parent.parent / "resources" / "databases" / "northwind.db"

# --------------------- OBTENER LOS 10 PRODUCTOS MÁS RENTABLES --------------------- #
# Abrir conexión a la db
conn  = sqlite3.connect(DB_PATH)

# Crear la query para obtener los 10 productos más rentables
query = '''
    SELECT p.ProductName, SUM(p.Price * od.Quantity) AS Revenue
    FROM OrderDetails od
    JOIN Products p
    ON od.ProductID = p.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

# Usar pandas para ejecutar la query y obtener un DataFrame con los resultados (ejecuta internamente cursores y cierra conexiones)
top_products = pd.read_sql_query(query, conn)

# Crear un gráfico de barras para mostrar los 10 productos más rentables
top_products.plot(x="ProductName", y="Revenue", kind="bar", figsize=(10, 5), legend=False)

# Configurar el título y las etiquetas de los ejes y rotar las etiquetas para que se vean mejor
plt.title("Top 10 Productos más rentables")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()

# --------------------- OBTENER LOS 10 EMPLEADOS MÁS EFECTIVOS --------------------- #
query = '''
    SELECT e.FirstName || " " || e.LastName AS Employee, COUNT(*) AS OrdersCount
    FROM Orders o
    JOIN Employees e
    ON o.EmployeeID = e.EmployeeID
    GROUP BY o.EmployeeID
    ORDER BY OrdersCount ASC
    LIMIT 3
'''

top_employees = pd.read_sql_query(query, conn)
top_employees.plot(x="Employee", y="OrdersCount", kind="bar", figsize=(10, 5), legend=False)

plt.title("Top 10 Empleados más efectivos")
plt.xlabel("Empleados")
plt.ylabel("Total vendido")
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()

# Cerrar la conexión a la db
conn.close()