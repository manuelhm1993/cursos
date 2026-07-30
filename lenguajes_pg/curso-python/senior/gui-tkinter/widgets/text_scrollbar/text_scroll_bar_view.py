import tkinter as tk
from widgets.entry.entry_view import EntryView

class TextScrollBarView(EntryView):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)

        self.dimension_integrity = False
        self.lista_formulario    = [
            "Nombre:", "Contraseña:", "Apellido:", "Dirección:"
        ]

    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        super()._crear_widgets_internos(frame)

        # Obtener el número de filas y columnas
        columns, rows = frame.grid_size()
        columns = 0

        tk.Label(frame, text="Comentarios:").grid(row=rows, column=columns, sticky="e", padx=10, pady=10)

        columns += 1

        # Crear el widget Text 
        comentarios = tk.Text(frame, width=15, height=5)
        comentarios.grid(row=rows, column=columns, sticky="e", padx=10, pady=10)

        # Crear el scroll y vincularlo
        scroll_comentarios= tk.Scrollbar(frame, command=comentarios.yview)
        scroll_comentarios.grid(row=rows, column=(columns + 1), sticky="nsew")

        # Establecer el ScrollBar en el Text
        comentarios.config(yscrollcommand=scroll_comentarios.set)

        rows += 1
        columns = 0