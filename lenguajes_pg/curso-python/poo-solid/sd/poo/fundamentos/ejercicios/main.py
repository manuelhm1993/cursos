# Importar la clase estudiante
from ejercicio1 import Estudiante

# Solicitar datos
nombre = input("Ingrese el nombre del estudiante: ").capitalize()
grado  = input("Ingrese el grado del estudiante: ").capitalize()
edad   = input("Ingrese la edad del estudiante: ")

# Validar edad
while not edad.isdigit() or not 4 < int(edad) <= 105:
    print("Error. La edad debe ser un número positivo entre: [4-105]")
    edad   = input("Ingrese la edad del estudiante: ")

# Instanciar la clase
estudiante = Estudiante(nombre, edad, grado)
estudiante.descripcion()

# Flag
finalizar = "n"

while finalizar != "y":
    estudiar  = input("¿Desea que el estudiante estudie? Escibir \"Estudiar\": ").lower()
    
    print(estudiante.estudiar() if estudiar == "estudiar" else "")
    
    finalizar = input("¿Desea finalizar el programa? (y/n): ").lower()