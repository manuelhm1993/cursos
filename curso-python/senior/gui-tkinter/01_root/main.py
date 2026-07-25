import tkinter as tk
from .primera_interface import App

# Punto de entrada del programa
if __name__ == "__main__":
    # Instanciamos la raíz de Tkinter
    root = tk.Tk()

    # Inyectamos la raíz en nuestra clase
    app = App(root)

    # Arrancamos el mainloop (bucle infinito que escucha eventos)
    root.mainloop()