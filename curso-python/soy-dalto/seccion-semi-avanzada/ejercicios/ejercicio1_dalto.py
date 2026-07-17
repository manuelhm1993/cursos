"""Tenemos 2 listas: una de nombres y otra de apellidos. Escribirlas de forma óptima
en un .txt con un for"""
from pathlib import Path

NAMES_PATH = Path(__file__).parent / "resources" / "ejercicio1_dalto.txt"

nombres   = ["Manuel", "Sugey", "Carlos", "Ender", "Fernando"]
apellidos = ["Henriquez", "Godoy", "Vera", "Paredes", "Barrera"]

datos = [*zip(nombres, apellidos)]

with open(NAMES_PATH, "w", encoding="UTF-8") as archivo:
    archivo.write("DATOS DE LOS USUARIOS: \n------------------------\n")

    # Bucle for en una sola línea
    archivo.writelines([f"- Nombre: {nombre}\n- Apellido: {apellido}\n------------------------\n" for nombre, apellido in zip(nombres, apellidos)])
    
    print("Archivo escrito correctamente")
