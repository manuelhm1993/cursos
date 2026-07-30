import calculos.areas as ca
import re

def validar_email(email: str) -> bool:
    """Valida una dirección de correo utilizando expresiones regulares

    Args:
        email (str): correo a evaluar

    Returns:
        bool: True o False dependiendo si es correcto o no

    Examples:
        >>> validar_email("manuelhm1993@gmail.com")
        True

        >>> validar_email("manuelhm1993gmail.com@")
        False

        >>> validar_email("manuelhm1993gmail.com")
        False

        >>> validar_email("manuelhm1993@gmail@.com")
        False
    """
    pattern = r"^[a-zA-Z0-9_.+ñÑ-]+@[a-zA-Z0-9ñÑ-]+\.[a-zA-Z0-9.-]+$"

    return True if re.search(pattern, email) else False

def prueba_documentacion():
    """Muestra el resultado de los métodos de la clase Areas y el funcionamiento del helper
    help y el atributo __doc__

    Args:
        N/A
    """

    resultado = f"El área del cuadrado es: {ca.Areas.area_cuadrado(3)}"
    
    # La propiedad __doc__ devuelve la documentación asociada
    documentacion = ca.Areas.area_cuadrado.__doc__

    print(resultado)
    print(documentacion)

    # La función help hace lo mismo que doc, pero no se necesita el print
    help(ca.Areas.area_triangulo)
    help(ca.Areas)

    # Se puede incluso documentar un módulo
    help(ca)