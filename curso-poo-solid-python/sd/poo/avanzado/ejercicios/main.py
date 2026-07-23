"""Crear un juego de fusión
- El juego consiste en crear personajes de un juego y que esos personajes se puedan
fusionar para formar personajes más poderosos que tengan más poder...

- Para ello deberemos cambiar el comportamiento del operador '+' para que cuando los
personajes se fusionen, salga un nuevo personaje con habilidades mejoradas.

Una posible fórmula es: el promedio de las habilidades de ambos, al cuadrado."""
from raza import Raza
from saiyajin import Saiyajin

def fusion(obj1: Raza, obj2: Raza):
    return obj1 + obj2

universo7: list[Raza] = [
    Saiyajin("Saiyajin", "Vegeta", "Final flash", 18000),
    Saiyajin("Saiyajin", "Gokú", "Kame hame ha", 8000)
]

for guerrero in universo7:
    print(f"{guerrero} \n{guerrero.atacar()}", end="\n\n")

vegeta, goku = universo7

goku.nombre_persona = "Kakarotto"

print(fusion(vegeta, goku))
