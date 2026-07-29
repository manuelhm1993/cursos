from ui.interfaces.interface_view import InterfaceView, tk

class MainView(InterfaceView):
    # ------------------------------ Método constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__(ancho, alto)
        self._size_integrity = False

        self._sub_menu_opciones = (
            ("BBDD", ("Conectar", "Salir")),
            ("Borrar", ("Borrar campos",)),
            ("CRUD", ("Crear", "Leer", "Actualizar", "Borrar")),
            ("Ayuda", ("Licencia", "Acerca de..."))
        )

        self._botones_crud = ("Create", "Read", "Update", "Delete")

        # Variables de estado, permiten conservar la referencia a los widgets
        self._id          = tk.StringVar()
        self._nombre      = tk.StringVar()
        self._password    = tk.StringVar()
        self._apellido    = tk.StringVar()
        self._direccion   = tk.StringVar()
        self._comentarios = None

        self._campos_form  = (
            ("ID:", self._id),
            ("Nombre:", self._nombre),
            ("Password:", self._password),
            ("Apellido:", self._apellido),
            ("Dirección:", self._direccion),
            ("Comentarios:", self._comentarios)
        )

    # ------------------------------ Métodos de interfaz
    def construir_frame(self, master: tk.Tk) -> tk.Frame:
        main_frame = tk.Frame(master, width=self.ancho, height=self.alto)
        main_frame.pack(expand=True, fill="both")

        main_frame.pack_propagate(not self._size_integrity)

        self._construir_widgets(main_frame)

        return main_frame

    # ------------------------------ Métodos de configuración
    def _construir_widgets(self, frame: tk.Frame) -> None:
        frame_formulario = tk.Frame(frame)
        frame_crud       = tk.Frame(frame)

        frame_formulario.pack(expand=True, fill="both")
        frame_crud.pack(expand=True, fill="both")

        self._construir_botones_crud(frame_crud)
        self._construir_formulario(frame_formulario)

    def _construir_formulario(self, frame: tk.Frame) -> None:
        for index, (campo, var) in enumerate(self._campos_form):

            tk.Label(frame, text=campo).grid(row=index, column=0, padx=10, pady=10, sticky="e")
            input = tk.Entry(frame, textvariable=var)

            if campo == "Comentarios:":
                self._comentarios = tk.Text(frame, width=15, height=5)
                scroll_comentarios = tk.Scrollbar(frame, orient="vertical", command=self._comentarios.yview)

                self._comentarios.config(yscrollcommand=scroll_comentarios.set)

                self._comentarios.grid(row=index, column=1, padx=10, pady=10, sticky="w")
                scroll_comentarios.grid(row=index, column=2, sticky="nsew")
                break

            if campo == "Password:":
                input.config(show="*")

            input.grid(row=index, column=1, padx=10, pady=10, sticky="w")


    def _construir_botones_crud(self, frame: tk.Frame) -> None:
        for index, label in enumerate(self._botones_crud):
            tk.Button(frame, text=label).grid(row=0, column=index, padx=10, pady=10)

    def construir_barra_menu(self, master: tk.Tk) -> None:
        barra_menu = tk.Menu(master)

        i = 0

        for sub_menu, opciones in self._sub_menu_opciones:
            menu = tk.Menu(barra_menu, tearoff=0)

            barra_menu.add_cascade(label=sub_menu, menu=menu)

            for opcion in opciones:
                i += 1
                menu.add_command(label=opcion, command=lambda n=i: print(f"pene {n}"))

        master.config(menu=barra_menu)

    # ------------------------------ Métodos de accesores
    @property
    def size_integrity(self) -> bool:
        return self._size_integrity

    @size_integrity.setter
    def size_integrity(self, estado: bool) -> None:
        self._size_integrity = estado