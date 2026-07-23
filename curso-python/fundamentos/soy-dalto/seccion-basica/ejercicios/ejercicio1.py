#Datos de entrada
mas_rapido = 2.5
mas_lento = 7
promedio = 4
curso_dalto = 1.5

#Diferencias de crudos
crudo_promedio = 5
crudo_dalto = 3.5

#Diferencias de duración
diferencia_mas_rapido = 100 - (curso_dalto / mas_rapido * 100)
diferencia_mas_lento = 100 - (curso_dalto / mas_lento * 100)
diferencia_promedio = 100 - (curso_dalto / promedio * 100)

#Calculando el porcentaje de tiempo vacío removido
tiempo_vacio_promedio = 100 - promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - curso_dalto * 1000 // crudo_dalto / 10

#Resultados
print(f"El curso de Dalto dura un {diferencia_mas_rapido:.2f}% menos que el más rápido.")
print(f"El curso de Dalto dura un {diferencia_mas_lento:.2f}% menos que el más lento.")
print(f"El curso de Dalto dura un {diferencia_promedio:.2f}% menos que el promedio.")
print(f"Un curso promedio elimina un {tiempo_vacio_promedio:.2f}%. de tiempo vacío.")
print(f"El curso de Dalto elimina un {tiempo_vacio_dalto:.2f}%. de tiempo vacío.")
print(f"Ver 10 horas de este curso equivale a ver {(promedio / curso_dalto * 10):.2f}% horas de otros cursos.")