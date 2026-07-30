def control_acceso(edad):
    if edad <= 0 or edad > 100:
        respuesta = "Edad no válida"
    elif edad < 18:
        respuesta = "Acceso denegado, eres menor de edad"
    else:
        respuesta = "Bienvenido"
    
    return respuesta

print("Club House - Entrada")

edad = int(input("Ingrese su edad: "))

print(control_acceso(edad))
