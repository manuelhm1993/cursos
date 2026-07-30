from functools import reduce

class CalculatorEngine:
    @staticmethod
    def sumar(*numeros: str) -> int:
        return sum(map(lambda n: int(n), numeros))
    
    @staticmethod
    def restar(*numeros: str) -> int:
        return reduce(lambda acumulado, numero: int(acumulado) - int(numero), numeros)

    @staticmethod
    def multiplicar(*numeros: str) -> int:
        return reduce(lambda acumulado, numero: int(acumulado) * int(numero), numeros)

    @staticmethod
    def dividir(*numeros: str) -> float:
        return reduce(lambda acumulado, numero: float(acumulado) / float(numero), numeros)