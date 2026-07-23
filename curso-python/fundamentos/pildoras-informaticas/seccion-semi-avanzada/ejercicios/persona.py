class Persona:
    __id_clase = 0

    def __init__(self, nombre: str, genero: str, edad: int):
        Persona.__id_clase += 1

        self.__nombre = nombre
        self.__genero = genero
        self.__edad   = edad
        self.__id     = Persona.__id_clase

        print(f"Se ha creado una persona nueva. Nombre: {self.__nombre}")
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_genero(self) -> str:
        return self.__genero
    
    def get_edad(self) -> int:
        return self.__edad
    
    def get_id(self) -> int:
        return self.__id
    
    def __str__(self) -> str:
        return f"- ID: {self.__id} \n- Nombre: {self.__nombre} \n- Género: {self.__genero} \n- Edad: {self.__edad}"
