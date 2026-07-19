""" Para no usar rutas absolutas se debe entender que python usa el directorio 
actual como __main__, la solución pasa por usar módulos como un paquete y ejecutar el código
desde la raíz.

En este caso, en la terminal debemos ubicarnos en seccion-semi-avanzada/
esa carpeta contiene:
modulos/funciones_buenas
modulos/routing

Eso significa que actuará como paquete y al ejecutar, se debe ejecutar por módulo, no
por script, es decir: 
- script: py modulos/routing/import_optimizado.py
- módulo: py -m modulos.routing.import_optimizado
"""
from modulos.funciones_buenas.saludar import saludar

#Uso directo
print(saludar("Manuel"))