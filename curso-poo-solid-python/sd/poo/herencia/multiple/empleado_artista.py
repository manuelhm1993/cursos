from persona import Persona
from artista import Artista

# Herencia múltiple
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre: str, edad: int, nacionalidad: str, habilidad: str, salario: float, empresa: str):
        # En la herencia múltiple se referencia la clase y se pasa el self al llamar al __init__ contrario de super
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)

        # Atributos propios de la clase EmpleadoArtista
        self.salario = salario
        self.empresa = empresa

    def presentarse(self) -> str:
        # En la clase hija da lo mismo llamar al método con super o con self siempre y cuando no se tenga un método con el mismo nombre
        # self.mostrar_habilidad()
        print(f"""Hola, soy {self.nombre}, {super().mostrar_habilidad().lower()} y trabajo en {self.empresa}""")