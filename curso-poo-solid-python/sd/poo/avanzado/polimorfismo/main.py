"""A diferencia de otros lenguajes el polimorfismo y el enlazado dinámico no está
obligado a seguir un modelo o jerarquía de herencia. En otros lenguajes, este ejercicio
debió definir una clase abstracta Animal de la cual heredarían Gato y Perro, esta
clase abstracta definiría el método sonido y sus subclases lo implementarían. En
Python todo es más sencillo."""
class Gato:
    def sonido(self) -> None:
        print("Miau")

class Perro:
    def sonido(self) -> None:
        print("Guau")

# Polimorfismo de función
def emitir_sonido(animal: object) -> None:
    animal.sonido()

# Lista de objetos animal
animales = [Gato(), Perro()]

# Polimorfismo de objeto
for animal in animales:
    emitir_sonido(animal)