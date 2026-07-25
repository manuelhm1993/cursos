import tkinter as tk
from ui.interfaces import ViewInterface
from core.settings import ASSETS_PATH

class LabelView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho  = ancho
        self._alto   = alto

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        # Aquí el master (root) es inyectado desde afuera
        main_frame = tk.Frame(master, width=self._ancho, height=self._alto)
        main_frame.pack(expand=True, fill="both")

        self._crear_widgets_internos(main_frame)
        
        return main_frame

    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        # El método place ubica por coordenadas el widget dentro de su contenedor
        tk.Label(frame, text="Hola Alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

        # Bug 1 resuelto: Pasamos a string y usamos el kwarg file=
        # ruta_logo = str(ASSETS_PATH / "logo.png")
        
        # # Bug 2 resuelto: Guardamos la imagen en el scope de la instancia (self)
        # self._logo = tk.PhotoImage(file=ruta_logo)
        
        # # Asignamos la imagen al Label
        # lbl_imagen = tk.Label(frame, image=self._logo)
        # lbl_imagen.place(x=100, y=200)