# Entendiendo la herencia, es trasladar el concepto literal a la programación
class Persona:
    def __init__(self, nombre: str, edad: str, nacionalidad: str):
        self.nombre       = nombre
        self.edad         = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self) -> None:
        print(f"Hola, soy {self.nombre} y estoy hablando...")