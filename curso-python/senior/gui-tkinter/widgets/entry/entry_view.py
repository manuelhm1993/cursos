import tkinter as tk
from ui.interfaces import ViewInterface

class EntryView(ViewInterface):
    # ------------------------------- Constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho               = ancho
        self._alto                = alto
        self._dimension_integrity = False
        self._lista_formulario    = [
            "Nombre:", "Contraseña:", "Apellido:", "Dirección de casa:"
        ]

    # ------------------------------- Decoradores
    @property
    def lista_formulario(self) -> list[str]:
        return self._lista_formulario

    @lista_formulario.setter
    def lista_formulario(self, elementos: list[str]) -> None:
        self._lista_formulario = elementos

    @property
    def dimension_integrity(self) -> bool:
        return self._dimension_integrity

    @dimension_integrity.setter
    def dimension_integrity(self, status: bool) -> None:
        self._dimension_integrity = status

    # ------------------------------- Método implementado de la clase abstracta
    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)

        # Le quitamos el poder al grid de aplastar nuestro frame
        frame.grid_propagate(not self._dimension_integrity)

        frame.pack(expand=True, fill="both")

        self._crear_widgets_internos(frame)
        
        return frame

    # ------------------------------- Métodos protegidos de uso interno
    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        self._crear_formulario(frame, self._lista_formulario)

        
    def _crear_formulario(self, frame, lista_elementos: list[str]) -> None:
        for index, elemento in enumerate(lista_elementos):
            tag = tk.Label(frame, text=elemento)
            text_box = tk.Entry(frame)

            if elemento == "Contraseña:":
                text_box.config(show="*")

            # index representa la fila directamente si asumimos 1 campo por fila
            tag.grid(row=index, column=0, sticky="e", padx=10, pady=10)
            text_box.grid(row=index, column=1, padx=10, pady=10, sticky="w")
        