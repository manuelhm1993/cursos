import tkinter as tk
from ui.interfaces import ViewInterface

class EntryView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto  = alto

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)

        # Le quitamos el poder al grid de aplastar nuestro frame
        frame.grid_propagate(False)

        frame.pack(expand=True, fill="both")

        self._crear_widgets_internos(frame)
        
        return frame

    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        lista_elementos: list[str] = ["Nombre:", "Contraseña:", "Apellido:", "Dirección de casa:"]
        self._crear_formulario(frame, lista_elementos)

        
    def _crear_formulario(self, frame, lista_elementos: list[str]) -> None:
        row    = 0
        column = 0

        for elemento in lista_elementos:
            tag      = tk.Label(frame, text=elemento)
            text_box = tk.Entry(frame)

            # Más configuraciones de Entry
            if elemento == "Contraseña:":
                text_box.config(show="*")

            # Sticky ubica los textos del label como un justificado con los puntos cardinales
            tag.grid(row=row, column=column, sticky="e", padx=10, pady=10)
            column += 1

            text_box.grid(row=row, column=column, padx=10, pady=10)
            column += 1

            if column == 2:
                row += 1
                column = 0
        