import tkinter as tk

# Se usan imports absolutos porque la ejecución del main pierde referencias relativas
from core.settings import ASSETS_PATH

class App:
    def __init__(self, root: tk.Tk) -> None:
        self.__root = root

        # Configuración inicial
        self.__root.title("GUI TKinter - Python Nivel Senior")
        self.__root.resizable(False, False)
        self.__root.iconbitmap(ASSETS_PATH / "favicon.ico")

        # Dimensionar y centrar dinámicamente
        self._centrar_ventana(ancho=650, alto=350)

        # El método config permite hacer muchas manipulaciones en el root
        self.__root.config(bg="blue")

    def _centrar_ventana(self, ancho: int, alto: int) -> None:
        """
        Calcula las dimensiones de la pantalla y centra la ventana principal.
        Equivalente a Toolkit.getScreenSize() y setBounds() en Java.
        """
        self.__root.update_idletasks() # Asegura que Tkinter haya leído la pantalla del SO

        ancho_pantalla = self.__root.winfo_screenwidth()
        alto_pantalla  = self.__root.winfo_screenheight()

        # Coordenadas exactas para el centro (deben ser enteros)
        x = int(((ancho_pantalla - ancho) / 2)) 
        y = int(((alto_pantalla - alto) / 2))

        # El formato string exigido por Tkinter: "650x350+X+Y"
        self.__root.geometry(f"{ancho}x{alto}+{x}+{y}")