from logic.user_model import UserModel

import tkinter as tk
import tkinter.messagebox as msg

class UserController:
    @staticmethod
    def feed_back(titulo, mensaje) -> None:
        mensajes = {
            "Éxito": msg.showinfo,
            "Aviso": msg.showwarning,
            "Error": msg.showerror
        }

        response = mensajes.get(titulo, msg.showerror)
        response(titulo, mensaje)

    @staticmethod
    def cerrar_app(root: tk.Tk) -> None:
        if msg.askyesno("Cerrar app", "¿Desea salir de la aplicación?"):
            root.destroy()

    @staticmethod
    def crear_tabla_usuarios() -> None:
        titulo, mensaje = UserModel.crear_tabla_usuarios()
        UserController.feed_back(titulo, mensaje)

    @staticmethod
    def crear(nombre_usuario: str, password: str, apellido: str, direccion: str, comentarios: str) -> None:
        usuario  = (nombre_usuario, password, apellido, direccion, comentarios)
        UserController.feed_back(*UserModel.crear_usuario(usuario))

    @staticmethod
    def leer(usuario_id: str) -> tuple:
        id       = (int(usuario_id),)
        response = UserModel.leer_usuario(id)

        return response

    @staticmethod
    def actualizar(usuario_id: str, nombre_usuario: str, password: str, apellido: str, direccion: str, comentarios: str) -> None:
        request  = (nombre_usuario, password, apellido, direccion, comentarios)
        id       = (int(usuario_id),)

        UserController.feed_back(*UserModel.actualizar_usuario(request, id))

    @staticmethod
    def borrar(usuario_id: str) -> None:
        id       = (int(usuario_id),)

        UserController.feed_back(*UserModel.borrar_usuario(id))