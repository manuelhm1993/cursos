import tkinter as tk
from ui.interfaces import ViewInterface

class CalculatorView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto  = alto
        self._dimension_integrity = False

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)

        frame.propagate(not self._dimension_integrity)

        frame.pack(expand=True, fill="both")

        self._crear_widgets(frame)

        return frame

    def _crear_widgets(self, frame: tk.Frame) -> None:
        pantalla = tk.Entry(frame)
        pantalla.pack()

    @property
    def dimension_integrity(self) -> bool:
        return self._dimension_integrity

    @dimension_integrity.setter
    def dimension_integrity(self, accion: bool) -> None:
        self._dimension_integrity = accion