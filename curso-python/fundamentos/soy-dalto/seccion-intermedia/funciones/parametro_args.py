# Forma no óptima de sumar valores infinitos
def suma_no_optimizada(lista):
    suma = 0

    for i in lista:
        suma += i
    
    return suma

# Utilizando el parámetro args: convierte una cantidad indefinida de valores en un iterable (tupla) y debe ir al final
def suma_optimizada(nombre, *numeros):
    # print(numeros) # args conviere los valores en una tupla
    return f"{nombre}, la suma de tus números es: {sum(numeros)}"

# Args para destructuración de datos
def suma_total(lista):
    # print(*lista) # args separa los números de una lista en datos individuales
    return sum([*lista])

resultado1 = suma_no_optimizada([5, 3, 9, 10, 20, 3])
resultado2 = suma_optimizada("Manuel", 5, 3, 9, 10, 20, 3)
resultado3 = suma_total([5, 3, 9, 10, 20, 3])

print(f"""Resultados:
    - Suma no optimizada: {resultado1}
    - Suma optimizada: {resultado2}
    - Suma total: {resultado3}
""")