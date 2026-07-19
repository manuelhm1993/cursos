# Creando una excepción propia
class MHException(Exception):
    def __init__(self, e):
        print(f"¡Impresionante! Cometiste el siguiente error: {e}")

# Lanzar una excepción
# raise MHException("Jajajaja, persona poco culta")

# Manejando la excepción
try:
    raise MHException("Jajajaja, persona poco culta")
except:
    print("¿Cómo vas a cometer este error?")