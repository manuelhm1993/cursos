from helpers import prueba_documentacion
from tests import (
        tdd_modulo_ca, 
        tdd_funcion_validar_email, 
        tdd_funcion_raiz_cuadrada
    )

# from calculos.avanzados import raiz_cuadrada

if __name__ == "__main__":
    # Pruebas unitarias - Si no retorna nada, pasó el test, al retornar hay error
    tdd_modulo_ca()
    tdd_funcion_validar_email()
    tdd_funcion_raiz_cuadrada()

    # raiz_cuadrada([9, -16, 25, 36])