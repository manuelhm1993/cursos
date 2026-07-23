class TanqueGasolina:
    def __init__(self, litros: float) -> None:
        self.__gasolina = litros

    def echar_gasolina(self, litros: float) -> None:
        self.__gasolina += litros
    
    def consumir_gasolina(self, litros: float) -> None:
        self.__gasolina -= litros

    def get_gasolina(self) -> float:
        return self.__gasolina