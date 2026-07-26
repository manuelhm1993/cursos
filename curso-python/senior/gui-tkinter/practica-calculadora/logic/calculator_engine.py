class CalculatorEngine:
    @staticmethod
    def sumar(*numeros):
        return sum(map(lambda n: int(n), numeros))