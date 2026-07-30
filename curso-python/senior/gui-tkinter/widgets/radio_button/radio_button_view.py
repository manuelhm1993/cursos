import tkinter as tk
from ui.interfaces import ViewInterface

class RadioButtonView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto  = alto

        # 1. Variables de control como Estado de la Instancia (Sobreviven en RAM)
        self._genero = tk.IntVar()

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)

        frame.propagate(True)

        frame.pack(expand=True, fill="both")

        self._construir_widgets(frame)

        return frame

    def _construir_widgets(self, frame: tk.Frame) -> None:
        # Valor por defecto del grupo genero
        self._genero.set(1)

        tk.Label(frame, text="Género").pack()

        # Género es el grupo de estos radios
        tk.Radiobutton(frame, text="Masculino", variable=self._genero, value=1, command=self._imprimir_datos).pack()
        tk.Radiobutton(frame, text="Femenino", variable=self._genero, value=2, command=self._imprimir_datos).pack()
        tk.Radiobutton(frame, text="Transformer", variable=self._genero, value=3, command=self._imprimir_datos).pack()

        self._tag_event = tk.Label(frame, text="")

        self._tag_event.pack()

    def _imprimir_datos(self):
        genero = {
            1: "Masculino",
            2: "Femenino",
            3: "Transformer"
        }

        self._tag_event.config(text=f"Género: {genero[self._genero.get()]}")