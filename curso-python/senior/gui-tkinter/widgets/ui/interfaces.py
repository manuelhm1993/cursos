from abc import ABC, abstractmethod
import tkinter as tk

class ViewInterface(ABC):
    @abstractmethod
    def build_frame(self, master: tk.Tk) -> tk.Frame:
        """
        Contrato obligatorio: Recibe el contenedor padre (master) 
        y retorna el Frame principal construido y empaquetado.
        """
        pass