conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

# Dependiendo de la perspectiva, conjunto 2 es un subconjunto del conjunto 1
resultado = conjunto2.issubset(conjunto1) 
resultado = conjunto2 <= conjunto1

print(resultado)

# Dependiendo de la perspectiva, conjunto 1 es un superconjunto del conjunto 2
resultado = conjunto1.issuperset(conjunto2) 
resultado = conjunto1 >= conjunto2

print(resultado)

# Verificar si los conjuntos son diferentes, si al menos hay un elemento común, no lo son
resultado = conjunto1.isdisjoint(conjunto2)

print(resultado)