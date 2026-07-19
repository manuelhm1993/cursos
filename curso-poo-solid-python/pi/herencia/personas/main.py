from persona import Persona
from empleado import Empleado

manuel = Persona("Manuel", 32, "Maracaibo")

manuel.descripcion()

# Comprobar si un objeto es instancia de una clase particular
print("Manuel es un empleado" if isinstance(manuel, (Empleado,)) else "Manuel no es un empleado")