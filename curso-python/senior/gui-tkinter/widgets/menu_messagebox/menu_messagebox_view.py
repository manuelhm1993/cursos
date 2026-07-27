from ui.interfaces import ViewInterface
import tkinter as tk
import tkinter.messagebox as msb # Los díalogos se importan aparte

class MenuMessageBox(ViewInterface):
    # ---------------------------------------- Método constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__()
        self._ancho = ancho
        self._alto  = alto

    # ---------------------------------------- Métodos de implementación de interfaz
    def build_frame(self, master: tk.Tk) -> tk.Frame:
        main_frame = tk.Frame(master, width=self._ancho, height=self._alto)

        main_frame.pack_propagate(False)
        main_frame.pack(expand=True, fill="both")

        # 1. Los menús deben ir en el root ya que son gestionados por el SO
        self._crear_menu_principal(master)

        # 2. Se crean los widgets en un frame principal como siempre
        self._crear_widgets(main_frame)

        return main_frame

    # ---------------------------------------- Métodos estáticos con decoradores
    @staticmethod
    def mostrar_info(title: str, msg: str) -> None:
        msb.showinfo(title, msg)

    @staticmethod
    def mostrar_advertencia(title: str, msg: str) -> None:
        msb.showwarning(title, msg)
    
    @staticmethod
    def salir_sistema(title: str, msg: str, root: tk.Tk) -> None:
        # if msb.askokcancel(title, msg):
        if msb.askquestion(title, msg) == "yes":
            root.destroy() # root.quit | lambda : sys.exit(0)

    # ---------------------------------------- Métodos privados, uso interno
    def _crear_menu_principal(self, master: tk.Tk) -> None:
        # Crear la barra de menú principal
        main_menu_bar = tk.Menu(master)

        # Crear los submenú que siguen siento menús, pero agregados a la barra
        menu_archivo      = tk.Menu(main_menu_bar, tearoff=0)
        menu_edicion      = tk.Menu(main_menu_bar, tearoff=0)
        menu_herramientas = tk.Menu(main_menu_bar, tearoff=0)
        menu_ayuda        = tk.Menu(main_menu_bar, tearoff=0)

        # Se crean los submenú u opciones de cada submenú
        menu_archivo.add_command(label="Nuevo", command=lambda : print("Crear nuevo archivo"))
        menu_archivo.add_command(label="Abrir", command=lambda : print("Abrir nuevo archivo"))
        menu_archivo.add_separator() # Línea divisoria
        menu_archivo.add_command(label="Guardar", command=lambda : print("Guardar cambios"))
        menu_archivo.add_command(label="Guardar como", command=lambda : print("Abrir ventana para guardar"))
        menu_archivo.add_separator() # Línea divisoria
        menu_archivo.add_command(label="Salir", command=lambda : MenuMessageBox.salir_sistema("Salir", "¿Desea salir del sistema?", master)) 

        menu_edicion.add_command(label="Copiar", command=lambda : print("Elemento copiado"))
        menu_edicion.add_command(label="Cortar", command=lambda : print("Elemento cortado"))
        menu_edicion.add_command(label="Pegar", command=lambda : print("Elemento pegado"))

        menu_ayuda.add_command(label="Licencia", command= lambda : MenuMessageBox.mostrar_advertencia("Licencia", "Producto bajo licencia GNU."))
        menu_ayuda.add_command(label="Acerca de...", command= lambda : MenuMessageBox.mostrar_info("Info", "- Desarrollado por: MHenriquez\n - Versión: 1.0.0\n- Fecha: Julio 2026\n- Programador: Ing. Manuel Henriquez"))

        # Agregar los submenú a la barra
        main_menu_bar.add_cascade(label="Archivo", menu=menu_archivo)
        main_menu_bar.add_cascade(label="Edición", menu=menu_edicion)
        main_menu_bar.add_cascade(label="Herramientas", menu=menu_herramientas)
        main_menu_bar.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Agregar la barra de menú completa a root
        master.config(menu=main_menu_bar)

    def _crear_widgets(self, frame: tk.Frame) -> None:
        pass