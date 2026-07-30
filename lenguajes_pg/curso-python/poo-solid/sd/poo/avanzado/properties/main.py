class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.__nombre = nombre
        self.__edad   = edad

    # Este decorador vuelve el método getter una property, el mismo comportamiento de C#
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    # Forma de establecer un setter property, el mismo comportamiento de C#
    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    # Un deleter permite eliminar de la memoria una propiedad, el mismo comportamiento de C++
    @nombre.deleter
    def nombre(self) -> None:
        del self.__nombre

# Instancia de clase
manuel = Persona("Manuel", 32)

# Eliminar la propiedad
# del manuel.nombre

# Llamar a la propiedad sin paréntesis para obtener el valor
print(manuel.nombre)

# Llamar a la propiedad sin paréntesis para modificar el valor
manuel.nombre = "Sugey"

print(manuel.nombre)