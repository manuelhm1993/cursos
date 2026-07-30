class Vehiculo:
    def __init__(self, marca: str, modelo: str):
        self.__marca     = marca
        self.__modelo    = modelo
        self.__en_marcha = False
        self.__acelerar  = False
        self.__frenar    = False

    def arranchar(self) -> None:
        self.__en_marcha = True

    def acelerar(self) -> None:
        self.__acelerar = True
    
    def frenar(self) -> None:
        self.__frenar = True
    
    def estado(self) -> None:
        print(f"""Características del vehículo: 
- Marca:      {self.__marca}
- Modelo:     {self.__modelo}
- En marcha:  {self.__en_marcha}
- Acelerando: {self.__acelerar}
- Frenando:   {self.__frenar}""")