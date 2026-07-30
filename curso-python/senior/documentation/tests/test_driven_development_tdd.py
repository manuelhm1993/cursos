import calculos.areas as ca
import helpers.funciones as hf
import calculos.avanzados as caa

import doctest

def tdd_funcion_validar_email():
    doctest.testmod(hf)

def tdd_modulo_ca():
    # Para las pruebas unitarias se requiere el módulo doctest, si no devuelve nada, entonces está correcto
    # Si hay un error, lo mostrará en consola, debe estar documentado el módulo y función con >>>
    doctest.testmod(ca)

def tdd_funcion_raiz_cuadrada():
    doctest.testmod(caa)