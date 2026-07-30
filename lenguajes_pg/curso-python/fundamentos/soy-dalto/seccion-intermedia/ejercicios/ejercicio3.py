# Representar la serie de Fibonacci a partir de un número: 0 1 1 2 3 5 8 13
num = int(input("Ingrese un número: "))

def fibonacci(n):
    a, b = 0, 1
    lista = [0]

    for i in range((num + 1)):
        if b > num: 
            return lista
        else:
            lista.append(b)

            a, b = b, (a + b)

print(fibonacci(num))