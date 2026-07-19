import re

def validar_rangos(rangos: list[str], pattern: str) -> list[str]:
    lista_rangos = [*filter(lambda r: re.findall(pattern, r), rangos)]

    return lista_rangos

nombres = ["Manuel", "Sugey", "Ender", "Fernando", "Carlos"]
pedidos = ["Ma1", "Se1", "Ma2", "Ba1", "Ma3", "Va1", "Va2", "Ma4", "MaA", "Ma5", "MaB", "MaC"]

# Todos los pedidos de Madrid
pattern = r"^Ma[0-9a-zA-Z]$"

print(validar_rangos(pedidos, pattern))