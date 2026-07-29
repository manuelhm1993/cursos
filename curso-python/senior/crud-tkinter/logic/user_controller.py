from logic.user_model import UserModel

class UserController:
    @staticmethod
    def crear_tabla_usuarios() -> tuple:
        return UserModel.crear_tabla_usuarios()

    @staticmethod
    def crear(nombre_usuario: str, password: str, apellido: str, direccion: str, comentarios: str) -> tuple:
        usuario  = (nombre_usuario, password, apellido, direccion, comentarios)
        response = UserModel.crear_usuario(usuario)

        return response

    @staticmethod
    def leer(usuario_id: str) -> tuple:
        id       = (int(usuario_id),)
        response = UserModel.leer_usuario(id)

        return response

    @staticmethod
    def actualizar(usuario_id: str, nombre_usuario: str, password: str, apellido: str, direccion: str, comentarios: str) -> tuple:
        request  = (nombre_usuario, password, apellido, direccion, comentarios)
        id       = (int(usuario_id),)
        response = UserModel.actualizar_usuario(request, id)

        return response

    @staticmethod
    def borrar(usuario_id: str) -> tuple:
        id       = (int(usuario_id),)
        response = UserModel.borrar_usuario(id)

        return response