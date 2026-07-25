import tkinter as tk
from core.settings import ASSETS_PATH
from widgets.app.view_interface import ViewInterface

class Root:
    def __init__(self, root: tk.Tk, title: str, view: tk.Frame, ancho: int, alto: int, favicon: str = ASSETS_PATH / "favicon.ico") -> None:
        self._root = root
        self._root.title(title)
        self._root.resizable(False, False)
        self._root.iconbitmap(favicon)

        # Inversión de control: Root le presta su ventana al Builder
        self._main_frame = view

        # Ahora sí, calcula las dimensiones del frame recién construido
        self._centrar_ventana()

    def _centrar_ventana(self) -> None:
        self._root.update_idletasks()

        ancho_pantalla = self._root.winfo_screenwidth()
        alto_pantalla  = self._root.winfo_screenheight()

        ancho = self._main_frame.winfo_width()
        alto  = self._main_frame.winfo_height()

        x = int((ancho_pantalla - ancho) / 2)
        y = int((alto_pantalla - alto) / 2)

        self._root.geometry(f"{ancho}x{alto}+{x}+{y}")