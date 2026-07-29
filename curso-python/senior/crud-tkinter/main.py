from ui import tk, BaseView, MainView
from logic import UserController

if __name__ == "__main__":
    # root = tk.Tk()

    # main_view = MainView(300, 450)
    # window    = BaseView(root, "MHenriquez CRUD - 28 de Julio 2026", main_view)

    conectar   = UserController.crear_tabla_usuarios()
    crear      = UserController.crear("Manuel", "pene", "Henriquez", "Mi casa", "Te amo Sugey")
    leer       = UserController.leer(1)
    actualizar = UserController.actualizar(1, "Sugey", "vagina", "Godoy", "Su casa", "Te amo Manuel")
    borrar     = UserController.borrar(1)

    print(conectar)
    print(crear)
    print(leer)
    print(actualizar)
    print(borrar)
    print(UserController.crear_tabla_usuarios())

    # root.mainloop()