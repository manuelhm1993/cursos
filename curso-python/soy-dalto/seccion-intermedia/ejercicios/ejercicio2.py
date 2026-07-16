# Crear una función que reciba un número y muestre números primos hasta llegar a él
def es_primo(num):
    cont  = 0
    primo = False

    for i in range(1, (num + 1)):
        if (num % i) == 0:
            cont += 1
        
        if cont == 2 and i != num:
            break

        if cont == 2 and i == num:
            primo = True
    
    return primo

num = int(input("Ingrese un número: "))

while num <= 1:
    print("El número debe ser mayor que 1")
    num = int(input("Ingrese un número: "))

lista_primos = [*filter(lambda n : es_primo(n), range(1, (num + 1)))]

print(lista_primos)