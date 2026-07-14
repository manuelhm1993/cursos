def control_acceso(edad):
    respuesta = "Edad no válida"

    if edad > 0 and edad <= 100:
        if edad < 18:
            respuesta = "Acceso denegado, eres menor de edad"
        else:
            respuesta = "Bienvenido"
    
    return respuesta

print("Club House - Entrada")

edad = int(input("Ingrese su edad: "))

print(control_acceso(edad))
