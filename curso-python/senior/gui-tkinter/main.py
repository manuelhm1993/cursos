import tkinter as tk
# from widgets.root.primera_interface import App
# from widgets.frame.uso_frames import App
# from widgets.label.label_view import LabelView
# from widgets.entry.entry_view import EntryView
from widgets.text_scrollbar.text_scroll_bar_view import TextScrollBarView
from ui.window import MainWindow

# Punto de entrada del programa
if __name__ == "__main__":
    # Instanciamos la raíz de Tkinter
    root = tk.Tk()

    # Instanciamos la vista concreta
    main_view = TextScrollBarView(1200, 600)

    # Inyectamos la raíz en nuestra clase
    app = MainWindow(root, "GUI TKinter - Uso Text & ScrollBar", main_view)
    app.redimensionar(False)

    # Arrancamos el mainloop (bucle infinito que escucha eventos)
    root.mainloop()