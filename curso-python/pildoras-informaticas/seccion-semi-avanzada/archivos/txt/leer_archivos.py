from pathlib import Path

FIEL_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

try:
    with open(FIEL_PATH, "r", encoding="UTF-8") as archivo:
        contenido = archivo.read()

        print(contenido)
        
except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no fue encontrado.")
except PermissionError:
    print(f"Error: No tienes permisos para leer el archivo '{archivo}'.")
except OSError as e:
    print(f"Ocurrió un error inesperado de entrada/salida: {e}")