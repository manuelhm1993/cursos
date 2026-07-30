class VehiculoElectrico():
    def __init__(self):
        self.__autonomia = 100
        self.__cargando  = False
    
    def cargar_energia(self):
        self.__cargando = True