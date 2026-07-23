class Ejemplo:
    def __init__(self):
        # En Python un equivalente de protected es iniciar el nombre de la propiedad con '_'
        self._atributo_protected = "Protected"
        # En Python un equivalente de private es iniciar el nombre de la propiedad con '__'
        self.__atributo_private  = "Private"

        def __metodo_privado(self):
            print("No se puede acceder fuera de la clase")

print("Prueba ve modificadores de acceso:")
objeto = Ejemplo()

# Se puede acceder a protected, pero no a private
print(objeto._atributo_protected)