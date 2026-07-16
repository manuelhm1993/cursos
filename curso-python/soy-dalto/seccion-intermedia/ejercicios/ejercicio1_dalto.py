"""Hoy faltó el profesor de clases y los chicos se organizaron para armar la suya
propia. Uno de los alumnos va a ser el profesor y otro va a ser su asistente.
1. Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar
los datos de mayor a menor
2. El mayor de la clase es el profesor y el menor es el asistente, ¿quién es el
asistente y quién es el profesor?
"""
def obtener_companieros(cantidad_companieros):
    companieros = []

    for i in range(cantidad_companieros):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        edad   = int(input(f"Ingrese la edad del alumno {i + 1}: "))
        companiero = (nombre, edad)

        companieros.append(companiero)
    
    companieros.sort(key=lambda c : c[1], reverse=True)

    profesor  = companieros[0][0]
    asistente = companieros[-1][0]

    return profesor, asistente

# Ordernar de mayor a menor
profesor, asistente = obtener_companieros(5)

print(f"""Facilitadores de la clase
    - Profesor: {profesor}
    - Asistente: {asistente}
""")