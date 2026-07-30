class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(F):
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    pass
    # Si el método hablar existiera, se le daría prioridad por sobreescritura
    # def hablar(self):
    #     print("Hola desde D")

# El MRO es el Method Resolution Order, se prioriza de izquierda a derecha la lectura de herencia
d = D()

# Al no indicarse otra cosa, se prioriza B porque es la que está más a la izquierda
# d.hablar()

# Para especificar qué método usar se llama explícitamente la clase y el método recibe el objeto como self
A.hablar(d)

# Jerarquía de herencia MRO: D > B > A > C > F > object
print(D.mro())