import tkinter as tk
from core.settings import ASSETS_PATH
from widgets.ui.interfaces import ViewInterface

class MainWindow:
    def __init__(self, root: tk.Tk, title: str, view: ViewInterface, favicon: str = ASSETS_PATH / "favicon.ico") -> None:
        self._root = root
        self._root.title(title)
        self._root.iconbitmap(favicon)

        # Inversión de control: Root le presta su ventana al Builder
        self._main_frame = view.build_frame(self._root)

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

    def redimensionar(self, accion: bool) -> None:
        self._root.resizable(False, False) if not accion else self._root.resizable(1, 1)