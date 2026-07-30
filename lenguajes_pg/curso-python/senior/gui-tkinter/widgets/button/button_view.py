import tkinter as tk
from widgets.text_scrollbar.text_scroll_bar_view import TextScrollBarView

class ButtonView(TextScrollBarView):
    def __init__(self, ancho: int, alto: int):
        super().__init__(ancho, alto)

    def _escribir_nombre(self):
        """Callback que reacciona al clic del botón."""
        
        # 1. Buscamos el objeto Entry en el diccionario heredado
        caja_nombre = self._entries["Nombre:"]
        
        # 2. Por buena práctica, borramos lo que tenga escrito (desde el index 0 hasta el final)
        caja_nombre.delete(0, tk.END)
        
        # 3. Insertamos el texto nuevo en la posición 0
        caja_nombre.insert(0, "Manuel")
        
        # Extra: Imprimamos en consola para verificar la lectura (método .get())
        print("Valor actual en la caja:", caja_nombre.get())

    def _crear_widgets_internos(self, frame: tk.Frame) -> None:
        super()._crear_widgets_internos(frame)

        # 1. Obtenemos el ancho en columnas y el alto en filas actual
        columns, rows = frame.grid_size()

        # 2. Crear el contenedor secundario para botones
        frame_botones = tk.Frame(frame)

        # 3. Le decimos que empiece en la columna 0 y abarque TODAS las columnas (columnspan=columns)
        frame_botones.grid(row=rows, column=0, columnspan=columns, pady=10)

        # 4. Dentro de frame_botones, pack() centrará el botón de forma natural
        boton = tk.Button(frame_botones, text="Enviar", command=self._escribir_nombre)
        boton.pack()