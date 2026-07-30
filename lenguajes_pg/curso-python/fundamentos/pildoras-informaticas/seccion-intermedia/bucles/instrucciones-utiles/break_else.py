email = input("Ingrese su correo: ")

for i in email:
    if i == '@':
        arroba = True
        break # Salir del bucle sin ejecutar el else
else:
    arroba = False # El else se ejecuta al terminar el bucle

print(arroba)