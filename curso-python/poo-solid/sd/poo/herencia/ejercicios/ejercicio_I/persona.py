class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad   = edad

    def descripcion(self) -> str:
        return f"Descripción: \n- Nombre: {self.nombre} \n- Edad: {self.edad}"