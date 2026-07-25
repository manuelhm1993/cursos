from abc import ABC, abstractmethod
import tkinter as tk

class ViewInterface(ABC):
    @abstractmethod
    def build(self) -> tk.Frame:
        # Este método obliga a construir un Frame con el master dado
        pass

    @abstractmethod
    def crear_widgets_internos(self) -> None:
        # Aquí empaquetaremos botones, labels, etc.
        pass