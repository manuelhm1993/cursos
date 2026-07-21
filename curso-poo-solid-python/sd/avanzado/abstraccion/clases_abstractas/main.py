from persona import Persona
from estudiante import Estudiante
from trabajador import Trabajador

"""Las clases abstractas no pueden ser instanciadas, solo definen la herencia, pero
se puede aplicar el enlazado dinámico y el principio de sustitución"""
# variable: tipo = valor
lista_personas: list[Persona] = [
    Estudiante("Manuel", 32, "Masculino", "Programación"),
    Trabajador("Manuel", 32, "Masculino", "Programador")
]

# Uso de la abstracción como definidor de herencia y polimorfismo
print("--- Ejecutando Polimorfismo ---")

for persona in lista_personas:
    persona.presentarse()     # Llama al método de la clase padre
    persona.hacer_actividad() # Llama a la implementación específica de cada hijo
    
    print("-" * 20)