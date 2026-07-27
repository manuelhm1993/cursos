import tkinter as tk
from ui.interfaces import ViewInterface
from core.settings import ASSETS_PATH

class CheckButtonView(ViewInterface):
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto  = alto

        # El garbadge collector elimina las variables de la memoria al terminar los métodos
        self._logo     = tk.PhotoImage(file=ASSETS_PATH / "widgets/logo-avion.gif")
        self._destinos = {
            "Playa": tk.IntVar(), 
            "Montaña": tk.IntVar(), 
            "Turismo rural": tk.IntVar()
        }
        # Receptora del evento
        self._confirmacion_viaje = None

    def build_frame(self, master: tk.Tk) -> tk.Frame:
        frame = tk.Frame(master, width=self._ancho, height=self._alto)
        frame.pack(expand=True, fill="both")

        frame.pack_propagate(False)

        self._construir_widgets(frame)

        return frame

    def _construir_widgets(self, frame: tk.Frame) -> None:
        tk.Label(frame, image=self._logo).pack(pady=(25, 10))
        tk.Label(frame, text="Elige un destino").pack(pady=(0, 10))

        for nombre_destino, variable_control in self._destinos.items():
            # El botón asigna 0-1 dependiendo del estado
            tk.Checkbutton(frame, text=nombre_destino, variable=variable_control, command=self._imprimir_destinos).pack()

        self._confirmacion_viaje = tk.Label(frame, text="")
        self._confirmacion_viaje.pack(pady=20)

    def _imprimir_destinos(self):
        # 1. Filtramos directamente los destinos que tengan valor 1 usando List Comprehension
        seleccionados = [destino for destino, variable in self._destinos.items() if variable.get() == 1]

        # 2. Guardia temprana (Early Return) verificando si la lista está vacía
        if not seleccionados:
            self._confirmacion_viaje.config(text="")
            return

        # 3. .join() se encarga de poner las comas mágicamente solo entre los elementos
        cadena = ", ".join(seleccionados)
        self._confirmacion_viaje.config(text=f"Itinerario: {cadena}")
