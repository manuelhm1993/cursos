"""Los métodos especiales son aquellas funciones que tienen un nombre reservado
inician y terminan con '__' como por ejemplo el método __init__ y su finalidad es
crear funcionalidades especiales que con métodos normales están fuera de alcance"""
class Persona:
    # Dunder method (método especial): constructor
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad   = edad

    # Dunder method (método especial): representa el objeto en texto
    def __str__(self) -> str:
        return f"Persona(nombre={self.__nombre}, edad={self.__edad})"
    
    # Dunder method (método especial): representa el objeto
    def __repr__(self) -> str:
        return f"Persona(\"{self.__nombre}\", {self.__edad})"
    
    # Sobrecarga de operadores: sobrecargar el operador + para indicar que pasa al sumar dos objetos Persona
    def __add__(self, other: Persona) -> int:
        experiencia = self.__edad + other.__edad
        return Persona(f"{self.__nombre} ❤️  {other.__nombre}", experiencia)

# --------------------- Instancias y llamadas a métodos --------------------- #
manuel = Persona("Manuel", 32)
sugey = Persona("Sugey", 22)

# Suma de edades
print(manuel + sugey)

repre = repr(sugey)
resultado = eval(repre)

print(manuel)
print(resultado)