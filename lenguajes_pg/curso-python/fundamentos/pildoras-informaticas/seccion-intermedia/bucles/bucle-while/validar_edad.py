def validar_numero(entrada):
    edad = 0

    if entrada.isnumeric():
        edad = int(entrada)
    
    return edad

edad = input("Ingrese su edad: ")
edad = validar_numero(edad)

while edad <=0 or edad >=100:
    print("Edad inválida")

    edad = input("Ingrese su edad: ")
    edad = validar_numero(edad)

print(f"Su edad es: {edad}")