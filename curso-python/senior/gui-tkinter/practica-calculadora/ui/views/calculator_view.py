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
        for index, (clave, valor) in enumerate(self._botones.items()):
            # divmod(index, 4) divide por 4 y te devuelve (cociente, residuo)
            # Ej: index 5 -> divmod(5, 4) = (1, 1) -> Fila 1, Columna 1
            # Importante: Para que no pise la pantalla (fila 0), sumamos 1 a la fila.
            row, col = divmod(index, 4)
            
            boton = tk.Button(frame, text=valor, width=3)
            boton.grid(row=(row + 1), column=col, padx=3, pady=3)
            
            self._ref_botones[clave] = boton

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