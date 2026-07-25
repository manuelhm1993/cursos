import tkinter as tk
# from widgets.root.primera_interface import App
# from widgets.frame.uso_frames import App
from widgets.label.label_view import LabelView
from widgets.ui.window import MainWindow

# Punto de entrada del programa
if __name__ == "__main__":
    # Instanciamos la raíz de Tkinter
    root = tk.Tk()

    # Instanciamos la vista concreta
    main_view = LabelView(500, 400)

    # Inyectamos la raíz en nuestra clase
    app = MainWindow(root, "GUI TKinter - Uso labels", main_view)
    app.redimensionar(True)

    # Arrancamos el mainloop (bucle infinito que escucha eventos)
    root.mainloop()