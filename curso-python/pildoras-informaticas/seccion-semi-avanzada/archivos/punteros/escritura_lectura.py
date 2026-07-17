from pathlib import Path

FIELD_PATH = Path(__file__).parent.parent / "resources" / "archivo.txt"

with open(FIELD_PATH, "r+", encoding="UTF-8") as archivo:
    lista_lineas = archivo.readlines()

    lista_lineas[2] = "Esto es todo con archivos .txt"

    archivo.seek(0)
    archivo.writelines(lista_lineas)
    archivo.seek(0)

    print(archivo.read())