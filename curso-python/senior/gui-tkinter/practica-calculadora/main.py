import tkinter as tk
from ui.window import MainView
from ui.views.calculator_view import CalculatorView

if __name__ == "__main__":
    root = tk.Tk()

    view = CalculatorView(600, 350)
    view.dimension_integrity = False

    app  = MainView(root, "Calculadora MHenriquez 2026", view)
    app.redimensionar(True)

    root.mainloop()