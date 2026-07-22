from raza import Raza

class Saiyajin(Raza):
    def __init__(self, nombre_raza: str, nombre_persona: str, nombre_ataque: str, poder_pelea: float) -> None:
        super().__init__(nombre_raza, nombre_persona, nombre_ataque, poder_pelea)

    def atacar(self) -> str:
        return f"Yo soy {self.nombre_persona} y mi ataque es: {self.nombre_ataque}"
    
    def __add__(self, other: Saiyajin) -> Saiyajin:
        # nombre: str        = f"{self.nombre_persona}-{other.nombre_persona}"
        nombre: str = self.nombre_persona[:-1] + other.nombre_persona[len(other.nombre_persona)-2:]
        nombre_ataque: str = f"{self.nombre_ataque}-{other.nombre_ataque}"

        # Calcular el poder de peleaal fusionarse: promedio del poder al cuadrado
        poder_pelea: float = ((self.poder_pelea + other.poder_pelea) / 2)**2

        return Saiyajin(self.nombre_raza, {nombre}, {nombre_ataque}, {poder_pelea})