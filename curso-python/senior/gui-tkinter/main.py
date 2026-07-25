import tkinter as tk
# from widgets.root.primera_interface import App
from widgets.frame.uso_frames import App

# Punto de entrada del programa
if __name__ == "__main__":
    # Instanciamos la raíz de Tkinter
    root = tk.Tk()

    # Inyectamos la raíz en nuestra clase
    app = App(root)

    # Arrancamos el mainloop (bucle infinito que escucha eventos)
    root.mainloop()