class Persona:
    def __init__(self, nombre: str, edad: str, nacionalidad: str):
        self.nombre       = nombre
        self.edad         = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self) -> str:
        return f"Hola, soy {self.nombre} y estoy hablando..."