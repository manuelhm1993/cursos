import calculos.areas as ca

def prueba_documentacion():
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