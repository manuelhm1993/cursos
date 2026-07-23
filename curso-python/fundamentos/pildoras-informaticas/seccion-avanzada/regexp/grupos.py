import re

def validar_generos(generos: list[str], pattern: str) -> list[str]:
    lista_generos = [*filter(lambda g: re.findall(pattern, g), generos)]

    return lista_generos

generos = ["Hombres", "Mujeres", "Mascotas", "Niñas", "Niños"]
pattern = r"Niñ[ao]s"

print(validar_generos(generos, pattern))