"""Importar un modulo dentro de una carpeta y darle un alias
import funciones.funciones_matematicas as f_matematicas

Invocar las funciones dentro del objeto modulo
f_matematicas.sumar(7, 5)
f_matematicas.restar(9, 5)"""

# Importar funciones individuales desde un módulo, si se quiere importar todo, se usa *
from funciones.funciones_matematicas import sumar, restar, multiplicar

sumar(7, 5)

restar(9, 5)

multiplicar(5, 6)