""" Un módulo es cualquier archivo .py. Estos permiten separar el proyecto en
partes y poder reutilizarlo, es decir, módulos pueden llamar a otros módulos.

Existen 3 tipos:
1. Módulos de python: estos están escritos en C, forman el core de python 
2. Módulos de terceros: son módulos creados por empresas y se pueden usar con pip como pandas
3. Módulos propios: son los módulos que creamos nosotros mismos
"""

# Importar un módulo y darle un alias. Esto creará la carpeta __pycache__ para uso de python, va en .gitignore
# import modulo_saludar as m_saludar

# saludo = m_saludar.saludar("Manuel")

# Forma de ver todo lo que tiene el módulo
# print(dir(m_saludar))

# Forma de ver el nombre del módulo
# print(m_saludar.__name__)


# Importar una función individual en lugar del módulo completo
from modulo_saludar import saludar, saludar_novia

saludo = saludar("Manuel")
saludo_novia = saludar_novia("mi amor")

print(saludo)
print(saludo_novia)