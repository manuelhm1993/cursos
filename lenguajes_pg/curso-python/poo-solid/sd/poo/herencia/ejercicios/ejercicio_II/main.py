""" Herencia - Ejercicio #3
Ejercicio de herencia múltiple y MRO:
- Imagina que estás modelando animales en un zoológico. Crear tres clases: "Animal",
"Mamífero" y "Ave". La clase "Animal" debe tener un método llamado "comer". La clase
"Mamífero" debe tener un método llamado "amamantar" y la clase "Ave" un método llamado
"volar".

- Ahora, crea una clase "Murciélago" que herede de "Mamífero" y "Ave", en ese orden, y
por lo tanto debe ser capaz de "amamantar" y "volar", además de "comer".

- Finalmente, juega con el orden de herencia de la clase "Murciélago" y observa cómo 
cambia el MRO y el comportamiento de los métodos al usar super()
"""
from murcielago import Murcielago

batman = Murcielago()

batman.comer()
batman.amamantar()
batman.volar()

# Murcielago > Mamifero > Ave > Animal > object
print(Murcielago.mro())