# Clase: plantilla que define las características comunes de objetos similares
class Celular:
    # Método constructor: método especial para dar estado inicial a los objetos
    def __init__(self, marca: str, modelo: str, camara: str):
        # Atributos de instancia
        self.marca  = marca
        self.modelo = modelo
        self.camara = camara

    # Los métodos son simplemente funciones, pero dentro de una clase, siempre reciben self
    def llamar(self) -> None:
        print(f"Estás haciendo una llamada desde un: {self.marca} - {self.modelo}")
    
    def colgar(self) -> None:
        print(f"Colgaste la llamada desde un: {self.marca} - {self.modelo}")

# Instanciar una clase o crear un obejto
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

# Acceder a los métodos de un objeto
celular2.llamar()
celular2.colgar()