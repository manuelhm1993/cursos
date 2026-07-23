email = input("Ingrese su correo: ")

def validar_email(email, bucle=False):
    arroba = False

    if bucle:
        for i in email:
            if i == '@':
                arroba = True
                break
    else:
        arroba = email.count("@") > 0
    
    return arroba

if validar_email(email, True):
    print(f"La dirección de correo: {email} es correcta")
else:
    print(f"La dirección de correo: {email} es incorrecta")