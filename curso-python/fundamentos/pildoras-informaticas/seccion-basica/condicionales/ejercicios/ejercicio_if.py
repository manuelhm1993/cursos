def evaluar_nota(nota):
    resultado = "Nota no válida"

    if nota > 0:
        resultado = "Aprobado"

        if nota < 9.5:
            resultado = "Reprobado"
    
    return resultado

print("Programa de evaluación de notas de alumnos")

nota = float(input("Ingrese la nota del alumno: "))

print(f"Resultado: {evaluar_nota(nota)}")