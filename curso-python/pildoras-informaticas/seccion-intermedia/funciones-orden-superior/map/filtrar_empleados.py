""" La función map es similar a filter, solo que es más potente debido a que no
aplica una simple condición, aplica una función a cada elemento de la lista a evaluar

- Los salarios no son anuales, son mensuales en este caso
"""
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
    
    def set_salario(self, salario):
        self.__salario = salario

empleados = [
    Empleado("Manuel", "Director", 1200),
    Empleado("Sugey", "Presidenta", 2000),
    Empleado("Carlos", "Administrativo", 500),
    Empleado("Fernando", "Front-end", 500),
    Empleado("Ender", "Técnico", 450)
]

def calcular_comision(empleado):
    # Aumentar el salario un 3% si el salario es inferior a $1000
    if empleado.get_salario() < 1000:
        empleado.set_salario(empleado.get_salario() * 1.03)

    return empleado

comisiones_empleados = map(calcular_comision, empleados)

print("""Empleados con un aumento del 3%
-----------------------------------------""")

for empleado in comisiones_empleados:
    print(empleado.__str__())