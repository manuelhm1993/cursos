# La abstracción es el proceso de crear una interfaz simple para ocultar toda la lógica interna de funcionamiento
class Auto:
    def __init__(self) -> None:
        self.__estado = "Apagado"

    def encender(self) -> None:
        self.__estado = "Encendido"

        print("El auto está encendido")
    
    # Abstracción del método encender para comprobación interna
    def conducir(self) -> None:
        if self.__estado == "Apagado":
            self.encender()
        
        print("Conduciendo el auto")