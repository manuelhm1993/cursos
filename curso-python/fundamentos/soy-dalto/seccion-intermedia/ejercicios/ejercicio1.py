"""Hoy faltó el profesor de clases y los chicos se organizaron para armar la suya
propia. Uno de los alumnos va a ser el profesor y otro va a ser su asistente.
1. Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar
los datos de mayor a menor
2. El mayor de la clase es el profesor y el menor es el asistente, ¿quién es el
asistente y quién es el profesor?
"""
def solicitar_datos():
    i = 0
    alumnos = []
    nombre = ""
    edad = 0
    final = 'y'

    while final != 'n':
        i += 1
        nombre = input(f"Ingrese el nombre del alumno {i}: ")
        edad = int(input(f"Ingrese la edad del alumno {i}: "))

        alumnos.append((nombre, edad))

        final = input("¿Desea agregar otro alumno? (y/n): ").lower()
    
    return alumnos

# Ordernar de mayor a menor
alumnos = solicitar_datos()
alumnos.sort(reverse=True, key=lambda a : a[1])

# Identificar al profesor y al asistente
profesor  = alumnos[0]
asistente = alumnos[-1]

print(f"""Listado de alumnos ordenado por edad de mayor a menor
    - Alumnos: {alumnos}
    - Profesor: {profesor}
    - Asistente: {asistente}
""")