from helpers import prueba_documentacion
from tests import tdd_modulo_ca, tdd_funcion_validar_email

if __name__ == "__main__":
    # Pruebas unitarias - Si no retorna nada, pasó el test, al retornar hay error
    tdd_modulo_ca()
    tdd_funcion_validar_email()