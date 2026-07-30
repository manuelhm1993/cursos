class Persona:
    def __init__(self, nombre: str, edad: int, residencia: str):
        self.__nombre     = nombre
        self.__edad       = edad
        self.__residencia = residencia
    
    def descripcion(self):
        print(f"""Descripción: 
- Nombre:              {self.__nombre}
- Edad:                {self.__edad}
- Lugar de residencia: {self.__residencia}""")