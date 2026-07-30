import tkinter as tk
from ui.interfaces import ViewInterface
from core.settings import ASSETS_PATH

class LabelView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho  = ancho
        self._alto   = alto
        self._logo = tk.PhotoImage(file=ASSETS_PATH / "widgets/logo-avion.gif")

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        # Aquí el master (root) es inyectado desde afuera
        main_frame = tk.Frame(master, width=self._ancho, height=self._alto)
        main_frame.pack(expand=True, fill="both")

        self._crear_widgets_internos(main_frame)
        
        return main_frame

    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        # El método place ubica por coordenadas el widget dentro de su contenedor
        # tk.Label(frame, text="Hola Alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)
        
        # Asignamos la imagen al Label
        tk.Label(frame, image=self._logo).place(x=100, y=200)