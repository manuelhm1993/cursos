from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, grado: str) -> None:
        super().__init__(nombre, edad)
        self.grado = grado

    def descripcion(self) -> str:
        return f"{super().descripcion()} \n- Grado: {self.grado}"