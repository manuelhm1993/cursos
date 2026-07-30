import calculos.areas as ca
import doctest

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

def test_driven_development_tdd():
    # Para las pruebas unitarias se requiere el módulo doctest, si no devuelve nada, entonces está correcto
    # Si hay un error, lo mostrará en consola, debe estar documentado el módulo y función con >>>
    doctest.testmod(ca)