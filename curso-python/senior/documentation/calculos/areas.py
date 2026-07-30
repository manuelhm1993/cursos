"""
==================================================================================
Este módulo tiene el objetivo de proveer clases y funciones para cálculos básicos 
I y II
=================================================================================="""

class Areas:
    # Para documentar una función se usa la triple comilla y dentro de la misma

    """
    ==================================================================================
    Clase que calcula las áreas de diferentes polígonos
    =================================================================================="""
    @staticmethod
    def area_cuadrado(lado: float) -> float:
        """
        ==================================================================================
        Función encargada de calcular el área de un cuadrado en base del lado pasado
        por parámetro
        =================================================================================="""
        return lado * lado

    @staticmethod
    def area_triangulo(base: float, altura: float) -> float:
        """
        ==================================================================================
        Función encargada de calcular el área de un triángulo usando los parámetros
        base y altura
        =================================================================================="""
        return (base * altura) / 2