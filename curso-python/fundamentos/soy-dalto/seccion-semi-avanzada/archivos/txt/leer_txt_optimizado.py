from pathlib import Path

FIELD_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

# Esta sintaxis permite que with abra y cierre el archivo al salir del bloque optimizando recursos
with open(FIELD_PATH, encoding="UTF-8") as archivo:
    contenido = archivo.read()

    print(contenido)

# archivo.close() no es necesario porque ya with lo hace