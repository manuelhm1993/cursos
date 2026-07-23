# Validar si está aprobado o reprobado según la nota
def evaluacion(nota):
    resultado = "Aprobado"
    
    if nota < 5:
        resultado = "Reprobado"
    
    return resultado

print(f"Resultado: {evaluacion(4)}")