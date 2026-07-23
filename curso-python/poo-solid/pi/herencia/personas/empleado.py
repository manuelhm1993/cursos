from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, residencia: str, salario: float, antiguedad: float):
        # Llamar al constructor padre
        super().__init__(nombre, edad, residencia)
        self.__salario    = salario
        self.__antiguedad = antiguedad

    def descripcion(self):
        # Llamar al método padre
        super().descripcion()
        print(f"""- Salario:             ${self.__salario:,.2f}
- Antigüedad en años:  {self.__antiguedad}""")