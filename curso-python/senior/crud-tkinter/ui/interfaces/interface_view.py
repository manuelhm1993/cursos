from abc import ABC, abstractmethod
import tkinter as tk

class InterfaceView(ABC):
    # ------------------------------------ Método constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto = alto

    # ------------------------------------ Métodos abstractos
    def construir_frame(self, master: tk.Tk) -> tk.Frame:
        pass

    # ------------------------------------ Métodos accesores
    @property
    def ancho(self) -> int:
        return self._ancho

    @ancho.setter
    def ancho(self, ancho: int) -> None:
        self._ancho = ancho

    @property
    def alto(self) -> int:
        return self._alto

    @alto.setter
    def alto(self, alto: int) -> None:
        self._alto = alto