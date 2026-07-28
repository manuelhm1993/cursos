from ui import tk, BaseView, MainView

if __name__ == "__main__":
    root = tk.Tk()

    main_view = MainView(300, 450)
    window    = BaseView(root, "MHenriquez CRUD - 28 de Julio 2026", main_view)

    root.mainloop()