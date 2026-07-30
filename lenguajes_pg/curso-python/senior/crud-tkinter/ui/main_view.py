from ui.interfaces.interface_view import InterfaceView, tk
from logic import UserController, UserModel

import tkinter.messagebox as msg

class MainView(InterfaceView):
    # ------------------------------ Método constructor
    def __init__(self, ancho: int, alto: int) -> None:
        super().__init__(ancho, alto)
        self._size_integrity = False

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

        self._licencia   = "MHenriquez - CRUD Tkinter Julio 2026\
            \n- Licencia GNU"
        self._acerca_de  = "MHenriquez - CRUD Tkinter\
            \n- Versión: 1.0\
            \n- Fecha: 29/07/2026\
            \n- Desarrollado por: Ing. Manuel Henriquez"

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
        botones_crud = (
            ("Create", self._create_usuario), 
            ("Read", lambda : self._set_usuario()), 
            ("Update", self._update_usuario), 
            ("Delete", self._delete_usuario)
        )

        for index, (label, comando) in enumerate(botones_crud):
            tk.Button(frame, text=label, command=comando).grid(row=0, column=index, padx=10, pady=10)

    def construir_barra_menu(self, master: tk.Tk) -> None:
        barra_menu = tk.Menu(master)

        sub_menu_opciones = (
            ("BBDD", (
                    ("Conectar", UserController.crear_tabla_usuarios), 
                    ("Salir", lambda : UserController.cerrar_app(master))
                )
            ),
            ("Borrar", (("Borrar campos", self._borrar_campos),)),
            ("CRUD", (
                    ("Crear", self._create_usuario), 
                    ("Leer", lambda : self._set_usuario()), 
                    ("Actualizar", self._update_usuario), 
                    ("Borrar", self._delete_usuario)
                )
            ),
            ("Ayuda", (
                    ("Licencia", lambda : msg.showinfo("Licencia", self._licencia)), 
                    ("Acerca de...", lambda : msg.showinfo("Acerca de", self._acerca_de))
                )
            )
        )

        for sub_menu, opciones in sub_menu_opciones:
            menu = tk.Menu(barra_menu, tearoff=0)
            barra_menu.add_cascade(label=sub_menu, menu=menu)

            for opcion, comando in opciones:
                menu.add_command(label=opcion, command=comando)

        master.config(menu=barra_menu)

    # ------------------------------ Métodos de eventos
    def _create_usuario(self):
        data = self._get_usuario(False)

        validated = tuple(filter(lambda d: d not in ("", "\n", "\t", "\r"), data))

        if len(validated) == 0:
            msg.showwarning("Aviso", "Debe ingresar al menos un campo")
            return

        UserController.crear(*self._get_usuario())

        ultimo_usuario = UserModel.ultimo_usuario()

        if ultimo_usuario[0] != "Error" and ultimo_usuario[0] is not None:
            self._set_usuario(ultimo_usuario)

    def _delete_usuario(self) -> None:
        usuario_id = self._get_usuario_id(False)

        if not usuario_id:
            msg.showwarning("Aviso", "Debe ingresar un id con valor")
            return
        
        UserController.borrar(usuario_id)

        self._borrar_campos()

    def _update_usuario(self) -> None:
        usuario_id = self._get_usuario_id(False)

        if not usuario_id:
            msg.showwarning("Aviso", "Debe ingresar un id con valor")
            return
        
        usuario = self._get_usuario(False)

        UserController.actualizar(usuario_id, *usuario)

        self._set_usuario()

    def _set_usuario(self, ultimo_usuario = None) -> None:
        if ultimo_usuario is None:
            usuario_id = self._get_usuario_id(False)

            if not usuario_id:
                msg.showwarning("Aviso", "Debe ingresar un id con valor")
                return

            usuario = UserController.leer(usuario_id)

            if not usuario:
                msg.showwarning("Aviso", "Usuario no encontrado")
                return
        else:
            usuario = ultimo_usuario

        for (campo_label, campo_var), usuario_valor in zip(self._campos_form, usuario):
            if campo_var is not None:
                campo_var.set(usuario_valor)
            else:
                self._comentarios.delete("1.0", "end")
                self._comentarios.insert("1.0", usuario_valor)

    def _get_usuario_id(self, borrar_campos = True) -> str:
        data = self._id.get()

        if borrar_campos:
            self._borrar_campos()

        return data

    def _get_usuario(self, borrar_campos = True) -> tuple:
        # Bucle for pitónico con operador ternario
        data = tuple(
            var.get() if isinstance(var, tk.StringVar) else self._comentarios.get("1.0", "end")
            # Validar que el ID no se tome en cuenta
            for campo, var in self._campos_form[1:]
        )

        if borrar_campos:
            self._borrar_campos()

        return data

    def _borrar_campos(self) -> None:
        for campo, var in self._campos_form:
            if isinstance(var, tk.StringVar):
                var.set("")
            elif self._comentarios is not None:
                self._comentarios.delete("1.0", "end")

    # ------------------------------ Métodos de accesores
    @property
    def size_integrity(self) -> bool:
        return self._size_integrity

    @size_integrity.setter
    def size_integrity(self, estado: bool) -> None:
        self._size_integrity = estado