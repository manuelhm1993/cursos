class Artista:
    def __init__(self, habilidad: str):
        self.habilidad = habilidad
    
    def mostrar_habilidad(self) -> str:
        return f"Mi habilidad es: {self.habilidad}"