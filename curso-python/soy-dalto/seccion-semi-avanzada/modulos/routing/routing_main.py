# Si el módulo está dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

# Si el módulo está en una carpeta fuera de la ruta
import sys

# Nombre de los módulos dentro de python
# print(sys.builtin_module_names)

# Instalar un módulo para una sesión particular (temporal)
sys.path.append('C:\\Users\\manue\\Documents\\Devs\\cursos\\curso-python\\soy-dalto\\seccion-semi-avanzada\\modulos\\funciones_buenas')

import saludar

print(saludar.saludar("Manuel"))