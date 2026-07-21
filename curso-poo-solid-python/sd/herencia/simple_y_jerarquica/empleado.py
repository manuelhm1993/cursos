from persona import Persona

# El principio de sustitución: "Es siempre un" - Un empleado siempre es una persona
class Empleado(Persona):
    def __init__(self, nombre: str, edad: str, nacionalidad: str, trabajo: str, salario: float):
        # El método super llama a la clase padre, en este caso al constructor
        super().__init__(nombre, edad, nacionalidad)

        # Propiedades específicas del empleado
        self.trabajo = trabajo
        self.salario = salario
