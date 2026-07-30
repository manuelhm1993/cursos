from persona import Persona
from artista import Artista
from empleado_artista import EmpleadoArtista
from typing import type

def validar_herencia(clase1: type, clase2: type) -> bool:
    return issubclass(clase1, clase2)

def validar_instancia(obj: EmpleadoArtista) -> bool:
    return isinstance(obj, Persona)

sugey = EmpleadoArtista("Sugey", 22, "Venezolana", "Cantar", 400, "Farma Vid")

print(validar_herencia(EmpleadoArtista, Persona))
print(validar_instancia(sugey))