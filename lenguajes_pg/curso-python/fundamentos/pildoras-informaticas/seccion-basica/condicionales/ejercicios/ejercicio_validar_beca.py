def validar_candidato(distancia_centro, cantidad_hermanos, salario_familiar):
    resultado = ""

    if (distancia_centro > 40 and cantidad_hermanos > 2) or salario_familiar <= 20000:
        resultado = "Postulante aprobado"
    else:
        resultado = "Postulante rechazado"
    
    print(resultado)

print("Programa de becas año 2026\n")

distancia_centro  = float(input("Ingrese la distancia en KM de su casa al centro: "))
cantidad_hermanos = int(input("Ingrese su número de hermanos: "))
salario_familiar  = float(input("Ingrese su salario familiar: "))

print(f"""\nDatos del postulante:
    - Distancia al centro: {distancia_centro}
    - Cantidad de hermanos: {cantidad_hermanos}
    - Salario familiar: {salario_familiar}
""")

validar_candidato(distancia_centro, cantidad_hermanos, salario_familiar)