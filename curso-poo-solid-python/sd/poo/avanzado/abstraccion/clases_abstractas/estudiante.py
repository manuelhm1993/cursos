from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, sexo: str, actividad: str) -> None:
        super().__init__(nombre, edad, sexo, actividad)

    # Implementar el método abstracto
    def hacer_actividad(self) -> None:
        print(f"Estoy estudiando {self.actividad}")