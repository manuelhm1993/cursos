from persona import Persona
from empleado import Empleado

# El objeto Manuel tiene todos los atributos de una persona al ser empleado
manuel = Empleado("Manuel", 32, "Venezolano", "Programador", 8500)

# Accediendo a un método heredado
manuel.hablar()