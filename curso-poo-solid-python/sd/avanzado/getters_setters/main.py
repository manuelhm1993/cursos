class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        # Propiedades encapsuladas
        self.__nombre = nombre
        self.__edad   = edad

    # Setters establecen los valores de una propiedad (definidores)
    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    # Getters devuelven los valores de una propiedad (accesores)
    def get_nombre(self) -> str:
        return self.__nombre

# Instancia de clase
manuel = Persona("Manuel", 32)

# Acceso correcto a una propiedad de clase desde afuera de la misma
print(manuel.get_nombre())

# Modificar una propiedad bajo los permisos apropiados
manuel.set_nombre("Sugey")

print(manuel.get_nombre())