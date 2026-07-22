"""DIP: principio de inversión de dependencias, dicta que los módulos de alto nivel
no tienen que depender de los módulos de bajo nivel, si no, que los dos dependen de las
abstracciones. Tampoco las abstracciones no dependen de los detalles, si no, los detalles
de las abstracciones"""

# Procesador de texto simulado. En este ejemplo CorrectorOrtografico depende de Diccionario y se viola el principio
# class Diccionario:
#     def validar_palabra(self, palabra: str) -> str:
#         # Lógica para validar las palabras
#         pass

# class CorrectorOrtografico:
#     def __init__(self, diccionario: Diccionario) -> None:
#         self.__diccionario = diccionario

#     def corregir_texto(self, texto: str) -> str:
#         # Lógica para corregir textos
#         pass

# Aplicando DIP
from abc import ABC, abstractmethod

class VerificadorOrtogradico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass

class Diccionario(VerificadorOrtogradico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el diccionario
        pass

class ServicioOnLine(VerificadorOrtogradico):
    def verificar_palabra(self, palabra):
        # Lógica para verificar palabras si está en el servicio on-line
        pass

class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtogradico):
        self.__verificador = verificador

    def corregir_texto(self, texto):
        # Usamos el verificador para corregir el texto, cualquier clase que implemente la interfaz
        pass