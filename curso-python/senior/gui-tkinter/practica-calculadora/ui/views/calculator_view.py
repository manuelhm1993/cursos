import tkinter as tk
from ui.interfaces import ViewInterface

class CalculatorView(ViewInterface):
    # --------------------------------- Método constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho               = ancho
        self._alto                = alto
        self._dimension_integrity = False
        self._pantalla            = None
        self._botones             = {
            "siete": "7",
            "ocho": "8",
            "nueve": "9",
            "dividir": "/",
            "cuatro": "4",
            "cinco": "5",
            "seis": "6",
            "multiplicar": "x",
            "uno": "1",
            "dos": "2",
            "tres": "3",
            "restar": "-",
            "punto": ".",
            "cero": "0",
            "igual": "=",
            "sumar": "+",
        }
        self._ref_botones: dict[str, tk.Button] = {}

    # --------------------------------- Método de interfaz: Constructore de main_frame
    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)

        frame.grid_propagate(not self._dimension_integrity)

        frame.pack(expand=True, fill="both")

        self._crear_widgets(frame)

        return frame

    # --------------------------------- Métodos privados: Constructores de widgets 
    def _crear_widgets(self, frame: tk.Frame) -> None:
        self._construir_pantalla(frame)
        self._construir_botones(frame)

    def _construir_botones(self, frame: tk.Frame) -> None:
        claves_valores = self._botones.items()
        i      = 0
        row    = 1
        column = 0

        for clave, valor in claves_valores:
            boton = tk.Button(frame, text=valor, width=3)
            boton.grid(row=row, column=column, padx=3, pady=3)

            self._ref_botones[clave] = boton

            if i > 0 and i % 3 == 0:
                row += 1
                column = 0
                i = 0
            else:
                column += 1
                i += 1

        # Liberar recursos que no se utilizarán de nuevo
        del self._botones

    def _construir_pantalla(self, frame: tk.Frame) -> None:
        self._pantalla = tk.Entry(frame, bg="#000000", fg="#03F943", justify="right")

        self._pantalla.insert(0, "0")
        self._pantalla.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

    # --------------------------------- Decoradores
    @property
    def dimension_integrity(self) -> bool:
        return self._dimension_integrity

    @dimension_integrity.setter
    def dimension_integrity(self, accion: bool) -> None:
        self._dimension_integrity = accion