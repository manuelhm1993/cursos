"""Tenemos 2 listas: una de nombres y otra de apellidos. Escribirlas de forma óptima
en un .txt con un for"""
from pathlib import Path

NAMES_PATH = Path(__file__).parent / "resources" / "ejercicio1.txt"

nombres   = ["Manuel", "Sugey", "Carlos", "Ender", "Fernando"]
apellidos = ["Henriquez", "Godoy", "Vera", "Paredes", "Barrera"]

datos = [*zip(nombres, apellidos)]

with open(NAMES_PATH, "w+", encoding="UTF-8") as archivo:
    archivo.write("Nombre | Apellido\n")
    
    for dato in datos:
        nombre, apellido = dato
        
        archivo.write(f"{nombre}  {apellido} \n")
    
    print("Archivo escrito correctamente")

    archivo.seek(0)

    contenido = archivo.read()
    
    print(contenido, end="")
