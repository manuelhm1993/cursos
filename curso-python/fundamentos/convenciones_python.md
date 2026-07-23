# 📐 Convenciones de Nomenclatura en Python (PEP 8)

| Elemento | Convención | Ejemplo Correcto |
| :--- | :--- | :--- |
| **Módulos (Archivos `.py`)** | `snake_case` o palabras cortas en minúscula. | `vehiculo.py`, `motor_electrico.py` |
| **Paquetes (Carpetas)** | Minúsculas, preferiblemente sin guiones bajos. | `modulos`, `routing` |
| **Clases** | `PascalCase` (Capitalizar cada palabra). | `Vehiculo`, `VehiculoMotorizado` |
| **Funciones y Métodos** | `snake_case` (minúsculas con guiones bajos). | `arrancar_motor()`, `frenar()` |
| **Variables** | `snake_case` (minúsculas con guiones bajos). | `velocidad_maxima`, `color` |
| **Constantes** | `SCREAMING_SNAKE_CASE` (todo mayúsculas). | `LIMITE_VELOCIDAD`, `PI` |

> **💡 Nota del Arquitecto:** Recuerda que los paquetes (carpetas) jamás deben llevar guiones medios (`-`) para evitar errores de sintaxis al importarlos, y siempre deben contener un archivo `__init__.py` (aunque esté vacío) para ser reconocidos formalmente por el ecosistema de Python.