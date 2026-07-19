edad = input("Ingrese su edad: ")

# Comprobar si se introdujo un número
if edad.isdigit():
    edad = int(edad)

    if 0<edad<100:
        if edad < 18:
            print("No puedes pasar")
        else:
            print("Puedes pasar")
    else:
        print("Edad inválida")
else:
    print("Edad inválida")