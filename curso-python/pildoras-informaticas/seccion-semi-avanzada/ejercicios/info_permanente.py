from persona import Persona
from lista_persona import ListaPersona

# persona1 = Persona("Manuel", "Masculino", 32)
# persona2 = Persona("Sugey", "Femenino", 22)
# persona3 = Persona("Ender", "Masculino", 30)

lp = ListaPersona()

# lp.agregar_persona(persona1)
# lp.agregar_persona(persona2)
# lp.agregar_persona(persona3)

lp.agregar_persona(Persona("John", "Masculino", 20))

lp.mostrar_personas()