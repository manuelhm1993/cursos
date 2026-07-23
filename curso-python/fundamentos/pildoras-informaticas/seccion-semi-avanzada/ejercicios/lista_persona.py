from persona import Persona
from pathlib import Path

import pickle

class ListaPersona:
    __LISTA_PERSONAS_PATH = Path(__file__).parent / "resources" / "lista_personas.pkl"

    def __init__(self):
        self.__personas: list[Persona] = []

        try:
            self.__personas = self.leer_binarios()
            print(f"Se cargaron {len(self.__personas)}")
        except:
            print("El fichero está vacío")

    def agregar_persona(self, persona: Persona) -> None:
        self.__personas.append(persona)

        self._guardado_permanente()

    def get_personas(self) -> list[Persona]:
        return self.__personas
    
    def mostrar_personas(self) -> None:
        for persona in self.__personas:
            print(persona, end="\n\n")

    def leer_binarios(self) -> object:
        with open(ListaPersona.__LISTA_PERSONAS_PATH, "ab+") as data_pkl:
            data_pkl.seek(0)
            data = pickle.load(data_pkl)
            
        return data

    def _guardado_permanente(self):
        # permiso = "ab+" if Path(ListaPersona.__LISTA_PERSONAS_PATH).is_file() else "wb"
        
        with open(ListaPersona.__LISTA_PERSONAS_PATH, "wb") as data_pkl:
            pickle.dump(self.__personas, data_pkl)
