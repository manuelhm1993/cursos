asignaturas = ("Informática gráfica", "Pruebas de software", "Usabilidad y accesibilidad")

print(f"""Asignaturas optativas año 2026
    1. {asignaturas[0]}
    2. {asignaturas[1]}
    3. {asignaturas[2]}
""")

eleccion = input("Ingrese la asignatura deseada: ")

if eleccion.isnumeric():
    eleccion = int(eleccion)

resultado = ""

if eleccion in asignaturas or eleccion in tuple(range(1, 4)):
    if type(eleccion) == int:
        resultado = f"Asignatura elegida: {asignaturas[eleccion - 1]}"
    else:
        resultado = f"Asignatura elegida: {eleccion}"
else:
    resultado = "Asignatura no contemplada"

print(resultado)