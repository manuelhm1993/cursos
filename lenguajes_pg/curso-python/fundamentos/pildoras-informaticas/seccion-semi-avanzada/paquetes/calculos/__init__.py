# paquetes/calculos/__init__.py

# Traemos los módulos desde las profundidades de nuestras carpetas
from .basicos.operaciones import sumar, restar, multiplicar, dividir
from .redondeo_potencia.operaciones import potenciar, redondear

# Definimos que queremos hacer público cuando alguien use nuestro paquete
__all__ = ["sumar", "restar", "multiplicar", "dividir", "potenciar", "redondear"]