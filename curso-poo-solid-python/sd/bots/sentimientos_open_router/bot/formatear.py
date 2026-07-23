from abc import ABC, abstractmethod

class Formatear(ABC):
    # Constantes de clase
    _RESET      = "\x1b[0m"      # Color original de la terminal
    _DEFAULT    = "\x1b[1;37m"   # Blanco
    _ROJO       = "\x1b[1;31m"   # Rojo
    _AMARILLO   = "\x1b[1;33m"  # Amarillo
    _VERDE      = "\x1b[1;32m"  # Verde

    @staticmethod
    @abstractmethod
    def formatear_texto(texto: str) -> str:
        pass