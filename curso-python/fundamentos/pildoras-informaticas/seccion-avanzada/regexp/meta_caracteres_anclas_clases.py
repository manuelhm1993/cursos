import re

def empleados_vip(empleados: list[str], pattern: str) -> list[str]:
    lista_vip = []

    for nombre in empleados:
        if re.findall(pattern, nombre):
            lista_vip.append(nombre)
    
    return lista_vip

def empleados_vip_filter(empleados: list[str], pattern: str) -> list[str]:
    lista_vip = [*filter(lambda e: re.findall(pattern, e), empleados)]

    return lista_vip

lista_nombres = [
    "Manuel Henriquez", 
    "Sugey Godoy", 
    "Santiago López", 
    "Sainer Gutierrez",
    "Carlos Vera"
]

# Comienza con 
# pattern = r"^Sa"

# Termina con 
pattern = r"ez$"

print(empleados_vip_filter(lista_nombres, pattern))