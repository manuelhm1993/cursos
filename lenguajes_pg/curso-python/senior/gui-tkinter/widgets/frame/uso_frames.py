import tkinter as tk
from core.settings import ASSETS_PATH

class App:
    def __init__(self, root: tk.Tk) -> None:
        self._root = root

        self._root.title("GUI TKinter - Uso Frames")
        self._root.iconbitmap(ASSETS_PATH / "favicon.ico")
        self._root.config(bg="blue")

        # Inicializamos la construcción de la UI
        self._crear_widgets()

    def _crear_widgets(self) -> None:
        self._crear_main_frame(600, 350)
        self._centrar_ventana()
        # Los futuros widgets irán empaquetados dentro de self._main_frame
    
    def _crear_main_frame(self, ancho: int, alto: int) -> None:
        # 1. Crear el Frame principal (Contenedor)
        self._main_frame = tk.Frame(self._root)

        self._main_frame.config(width=ancho, height=alto, bg="blue", relief="groove", bd=35, cursor="hand2")

        # 2. Empaquetar el Frame (El layout manager 'pack' lo ubica en la ventana)
        # fill=tk.BOTH y expand=True hacen que el Frame ocupe toda la ventana raíz
        self._main_frame.pack(expand=True, fill="both")

        # 3. El Frame también se adapta a su contenido, usar padding o
        # self._main_frame.pack_propagate(False)

    def _centrar_ventana(self) -> None:
        self._root.update_idletasks()

        ancho_pantalla = self._root.winfo_screenwidth()
        alto_pantalla  = self._root.winfo_screenheight()

        # El root siempre se adaptará al tamaño de sus componentes
        ancho = self._main_frame.winfo_width()
        alto  = self._main_frame.winfo_height()

        x = int(((ancho_pantalla - ancho) / 2))
        y = int(((alto_pantalla - alto) / 2))

        self._root.geometry(f"{ancho}x{alto}+{x}+{y}")