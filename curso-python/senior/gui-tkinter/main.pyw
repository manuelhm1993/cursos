import tkinter as tk
from widgets.menu_messagebox.menu_messagebox_view import MenuMessageBox
from ui.window import MainWindow

# Punto de entrada del programa
if __name__ == "__main__":
    # Instanciamos la raíz de Tkinter
    root = tk.Tk()

    # Instanciamos la vista concreta
    main_view = MenuMessageBox(300, 300)

    # Inyectamos la raíz en nuestra clase
    app = MainWindow(root, "GUI TKinter - Uso Menu & Messagebox", main_view)
    app.redimensionar(True)

    # Arrancamos el mainloop (bucle infinito que escucha eventos)
    root.mainloop()