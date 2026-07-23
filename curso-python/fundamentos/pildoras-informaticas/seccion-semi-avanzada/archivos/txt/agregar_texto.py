from pathlib import Path

FIEL_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

try:
    with open(FIEL_PATH, "a", encoding="UTF-8") as archivo:
        archivo.write("\nNueva línea de texto")

        print("Archivo modificado correctamente")

except FileNotFoundError:
    print(f"Error: El archivo '{archivo}' no fue encontrado.")
except PermissionError:
    print(f"Error: No tienes permisos para leer el archivo '{archivo}'.")
except OSError as e:
    print(f"Ocurrió un error inesperado de entrada/salida: {e}")