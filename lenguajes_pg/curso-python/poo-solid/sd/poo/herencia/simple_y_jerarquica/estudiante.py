from persona import Persona

# Herencia jerárquica, una superclase tiene muchas subclases
class Estudiante(Persona):
    def __init__(self, nombre: str, edad: str, nacionalidad: str, notas: list[float], instituto: str):
        # El método super llama a la clase padre, en este caso al constructor
        super().__init__(nombre, edad, nacionalidad)

        # Propiedades específicas del estudiante
        self.notas     = notas
        self.instituto = instituto
