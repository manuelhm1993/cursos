import tkinter as tk
from core.settings import ASSETS
from ui.interfaces import ViewInterface

class MainView:
    def __init__(self, root: tk.Tk, title: str, view: ViewInterface, favicon: str = ASSETS / "favicon.ico") -> None:
        self._root = root
        self._root.title(title)
        self._root.iconbitmap(favicon)

        self._main_frame = view.build_frame(self._root)
        
        self.centrar_ventana()

    def centrar_ventana(self) -> None:
        self._root.update_idletasks()

        ancho_pantalla = self._root.winfo_screenwidth()
        alto_pantalla  = self._root.winfo_screenheight()

        ancho = self._main_frame.winfo_width()
        alto  = self._main_frame.winfo_height()

        x = int(((ancho_pantalla - ancho) / 2))
        y = int(((alto_pantalla - alto) / 2))

        self._root.geometry(f"{ancho}x{alto}+{x}+{y}")

    def redimensionar(self, accion: bool) -> None:
        self._root.resizable(True, True) if accion else self._root.resizable(False, False)