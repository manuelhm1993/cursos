from core.settings import ASSETS
from ui.interfaces.interface_view import InterfaceView, tk

class BaseView:
    # ---------------------------- Método constructor
    def __init__(self, root: tk.Tk, titulo: str, view: InterfaceView, favicon: str = ASSETS / "favicon.ico") -> None:
        self._root = root

        self._root.title(titulo)
        self._root.iconbitmap(favicon)

        # Casting a MainView por enlazado dinámico, Python lo hace internamente
        view.construir_barra_menu(self._root)

        self._main_frame = view.construir_frame(self._root)

        self.centrar_ventana()
        self.redimensionar(False)

    # ---------------------------- Métodos de configuración
    def centrar_ventana(self) -> None:
        self._root.update_idletasks()

        ancho_pantalla = self._root.winfo_screenwidth()
        alto_pantalla  = self._root.winfo_screenheight()

        ancho_ventana = self._main_frame.winfo_width()
        alto_ventana  = self._main_frame.winfo_height()

        x = int(((ancho_pantalla - ancho_ventana) / 2))
        y = int(((alto_pantalla - alto_ventana) / 2))

        self._root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    def redimensionar(self, accion: bool) -> None:
        self._root.resizable(True, True) if accion else self._root.resizable(False, False)