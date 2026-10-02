import os
import shutil

from pathlib import Path

# Ruta base o raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent

# Ruta de la carpeta con los documentos a ordenar
DOCS_PATH = BASE_DIR / "docs"

# Parte I - Crear carpetas por tipo de documento
#
# 1. Crear una lista de carpetas por tipo de documento
tipos = ["PDFs", "Documentos_txt"]

# 2. Crear las carpetas por cada tipo de archivo
for tipo in tipos:
    path = os.path.join(DOCS_PATH, tipo)

    if not os.path.exists(path):
        os.makedirs(path)

# Parte II - Organizar cada archivo en su carpeta correspondiente según su tipo
#
# 1. Obtener la lista de archivos y documentos de la carpeta 
archivos = os.listdir(DOCS_PATH)

# 2. Crear un diccionario para el lookup table
extensiones = {
    "pdf": "PDFs",
    "txt": "Documentos_txt",
}

# 3. Recorrer los archivos de la carpeta y moverlos a su carpeta correspondiente
for archivo in archivos:
    lista = archivo.split(".")

    if len(lista) > 1:
        carpeta = extensiones.get(lista[1], "Error")

        shutil.move(DOCS_PATH / archivo, DOCS_PATH / carpeta / archivo)