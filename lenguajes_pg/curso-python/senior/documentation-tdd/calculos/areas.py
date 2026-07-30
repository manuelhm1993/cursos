"""Este módulo tiene el objetivo de proveer clases y funciones para cálculos básicos I y II
"""
class Areas:
    """Clase con métodos static para no necesitar instanciar la clase al realizar un
    cálculo básico.

    Attributes:
        N/A.
    """
    @staticmethod
    def area_cuadrado(lado: float) -> float:
        """Calcula el área de un cuadrado en base al lado pasado por parámetro

        Args:
            lado (float): Lado del cuadrado.

        Returns:
            float: Un valor flotante con el resultado del cálculo del área del cuadrado.

        Raises:
            TypeError: Si no se le pasa ningún parámetro.

        Examples:
            >>> Areas.area_cuadrado(3.0)
            9.0
        """
        return lado * lado

    @staticmethod
    def area_triangulo(base: float, altura: float) -> str:
        """Calcula el área de un cuadrado en base al lado pasado por parámetro
        
        Args:
            base   (float): Base del triángulo.
            altura (float): Altura del triángulo.

        Returns:
            str: Una cadena de texto indicando el resultado de la operación

        Raises:
            TypeError: Si no se le pasa ningún parámetro.

        Examples:
            >>> Areas.area_triangulo(3, 6)
            'El área del triángulo es: 9.0'

            >>> Areas.area_triangulo(4, 5)
            'El área del triángulo es: 10.0'

            >>> Areas.area_triangulo(9, 3)
            'El área del triángulo es: 13.5'
        """
        return f"El área del triángulo es: {(base * altura) / 2}"