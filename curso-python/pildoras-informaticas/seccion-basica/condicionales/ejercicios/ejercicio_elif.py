def validar_rango(nota):
    resultado = ""

    if nota >= 0 and nota <= 20:
        if nota <= 9.4:
            resultado = "Reprobado"
        elif nota <= 14:
            resultado = "Aprobado"
        elif nota <= 16:
            resultado = "Bueno"
        elif nota <= 18:
            resultado = "Distinguido"
        else:
            resultado = "Sobresaliente"
    else:
        resultado = "Nota inválida"

    print(resultado)

print("Rango de distinción por notas del alumno")

nota = float(input("Ingrese la nota: "))

validar_rango(nota)