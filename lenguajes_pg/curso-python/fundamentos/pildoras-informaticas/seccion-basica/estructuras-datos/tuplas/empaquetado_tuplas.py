# Empaquetar una tupla a partir de datos
tupla = "Manuel", 23, 7, 1993

print(tupla)

# Desempaquetado de tuplas, es el proceso contrario
nombre, dia, mes, anio = tupla

print(f"""Usuario:
    - Nombre: {nombre}
    - Fecha de nacimiento: {dia}/{mes}/{anio}
""")