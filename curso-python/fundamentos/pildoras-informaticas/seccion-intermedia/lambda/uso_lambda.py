# Las funciones lambda son funciones anónimas que permiten reducir el código

# Función tradicional
def area_triangulo(b, h):
    return (b * h) / 2

# Función lambda
area = lambda b, h : (b * h) / 2

t1 = area_triangulo(5, 7)
t2 = area_triangulo(9, 6)
t3 = area(5, 7)
t4 = area(9, 6)

print(f"""Cálculo del área de un triángulo
    - Función tradicional: t1:{t1} - t2:{t2}
    - Función lambda: t3:{t3} - t4:{t4}
""")