""" Crear una clase que permita crear objetos de tipo empleado y filtrar 
aquellos que tengan un salario superior a $50000"""
class Empleado:
    # Método constructor
    def __init__(self, nombre, cargo, salario):
        self.__nombre  = nombre
        self.__cargo   = cargo
        self.__salario = salario
    
    def __str__(self):
        return f"""Datos del empleado:
- Nombre: {self.__nombre}
- Cargo: {self.__cargo}
- Salario: ${self.__salario}
"""
    
    def get_salario(self):
        return self.__salario

empleados = [
    Empleado("Manuel", "Director", 75000),
    Empleado("Sugey", "Presidenta", 85000),
    Empleado("Carlos", "Administrativo", 25000),
    Empleado("Fernando", "Front-end", 27000),
    Empleado("Ender", "Técnico", 20000)
]

empleados_mayor_salario = filter(lambda e: e.get_salario() > 50000, empleados)

print("""Empleados con mayor salario
-----------------------------------------""")

for empleado in empleados_mayor_salario:
    print(empleado.__str__())