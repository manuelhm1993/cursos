class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca     = marca
        self.__modelo    = modelo
        self.__en_marcha = False
        self.__acelerar  = False
        self.__frenar    = False
    
    def arrancar(self):
        self.__en_marcha = True
    
    def acelerar(self):
        self.__acelerar = True
    
    def frenar(self):
        self.__frenar = True
    
    def estado(self):
        return f"""- Marca: {self.__marca}
- Modelo: {self.__modelo}
- En marcha: {self.__en_marcha}
- Acelerando: {self.__acelerar}
- Frenando: {self.__frenar}"""