from functools import reduce

class CalculatorEngine:
    @staticmethod
    def sumar(*numeros: int) -> int:
        return sum(map(lambda n: int(n), numeros))
    
    @staticmethod
    def restar(*numeros: int) -> int:
        return reduce(lambda acumulado, numero: int(acumulado) - int(numero), numeros)

    @staticmethod
    def multiplicar(*numeros: int) -> int:
        return reduce(lambda acumulado, numero: int(acumulado) * int(numero), numeros)

    @staticmethod
    def dividir(*numeros: float) -> float:
        return reduce(lambda acumulado, numero: float(acumulado) / float(numero), numeros)