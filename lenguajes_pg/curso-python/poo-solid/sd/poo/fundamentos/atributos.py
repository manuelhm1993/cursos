# Clase: plantilla que define las características comunes de objetos similares
class Celular:
    # Método constructor: método especial para dar estado inicial a los objetos
    def __init__(self, marca, modelo, camara):
        # Atributos de instancia
        self.marca  = marca
        self.modelo = modelo
        self.camara = camara

# Instanciar una clase o crear un obejto
celular1 = Celular("Samsung", "S23", "48MP")
celular2 = Celular("Apple", "Iphone 15 Pro", "96MP")

# Acceder a las propiedades de un objeto
print(celular1.marca)
print(celular2.marca)