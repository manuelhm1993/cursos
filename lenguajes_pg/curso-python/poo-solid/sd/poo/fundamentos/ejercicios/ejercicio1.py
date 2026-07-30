"""Crear el siguiente modelo
Clase:
    - Estudiante
        * Atributos:
            - Nombre
            - Edad
            - Grado
        * Métodos:
            - Estudiar: "El estudiante (nombre) está estudiando"

Instancias:
1. Se debe interactuar con el usuario y este debe brindar los atributos
2. Luego de solicitar los datos se debe instanciar la clase y mostrar sus atributos
3. Al escribir: "estudiar" el estudiante debe estudiar sin tomar en cuenta mayúsculas ni minúsculas
""" 
class Estudiante:
    def __init__(self, nombre: str, edad: str, grado: str):
        self.nombre = nombre
        self.edad   = edad
        self.grado  = grado
    
    def estudiar(self) -> str:
        return f"El estudiante {self.nombre} está estudiando."
    
    def descripcion(self) -> None:
        print(f"""Datos del estudiante:
- Nombre: {self.nombre}
- Edad:   {self.edad}
- Grado:  {self.grado}""")