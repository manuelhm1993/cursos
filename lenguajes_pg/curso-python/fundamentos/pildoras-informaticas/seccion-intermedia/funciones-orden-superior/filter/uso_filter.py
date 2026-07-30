# Las funciones de orden superior nos introducen en la programación funcional
def numeros_pares(numeros):
    pares = []

    for i in numeros:
        if (i % 2) == 0:
            pares.append(i)
    
    return pares

lista_numeros = [*range(1, 11)]

pares_fn = numeros_pares(lista_numeros)
pares_filter = [*filter(lambda i: (i % 2) == 0, lista_numeros)]

print(f"""Lista de números: {lista_numeros}
    - Pares con función normal: {pares_fn}
    - Pares con filter: {pares_filter}
""")