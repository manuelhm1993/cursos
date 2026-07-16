# Hallar los números pares de una lista
def get_pares(numeros):
    pares = []

    for i in numeros:
        if (i % 2) == 0:
            pares.append(i)
    
    return pares

numeros = list(range(1, 10))
numeros.extend([11, 13, 14, 15, 20])

pares_fn = get_pares(numeros)
pares_filter = filter(lambda n : (n % 2) == 0, numeros)

print(f"""Lista de números: {numeros}
    - Los números pares fn son: {pares_fn}
    - Los números pares filter son: {[*pares_filter]}
""")
