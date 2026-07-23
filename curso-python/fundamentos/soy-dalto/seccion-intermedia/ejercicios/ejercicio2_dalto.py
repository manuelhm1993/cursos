# Crear una función que reciba un número y muestre números primos hasta llegar a él
def es_primo(num):
    primo = False

    for i in range(2, num):
        if (num % i) == 0: break
    else:
        primo = True
    
    return primo

def primos_hasta(num):
    primos = []

    for i in range(1, (num + 1)):
        resultado = es_primo(i)

        if resultado:
            primos.append(i)
    
    return primos

print(primos_hasta(17))