lista = [4, 7, 1, 42, 15]

# Encontrar el mayor número de un iterable con valores numéricos
max_lista = max(lista)

# Encontrar el menor número de un iterable con valores numéricos
min_lista = min(lista)

# Redondear a 2 decimales
numero = round(12.345678, 2)

# Función para validar datos: False = 0, vacío, False, None || True = != 0, True o datos con valor
resultado_bool = bool(None)

# Función para validar datos: Ture = si todos los valores son True
resultado_all = all([None, "True", [344, 23]])

# Sumar todos los valores de un iterable con valores numéricos
suma_total = sum(lista)

print(f"""Lista: {lista}
    - Número máximo: {max_lista}
    - Número mínimo: {min_lista}
    - Redondeo:      {numero}
    - Booleano:      {resultado_bool}
    - All:           {resultado_all}
    - Sumatoria:     {suma_total}
""")