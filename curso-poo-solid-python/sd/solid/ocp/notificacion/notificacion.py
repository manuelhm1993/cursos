from ..usuario import Usuario

class Notificacion:
    def __init__(self, usuario: Usuario, mensaje: str) -> None:
        self.__usuario = usuario
        self.__mensaje = mensaje

    def notificar(self):
        raise NotImplementedError

    @property
    def usuario(self) -> Usuario:
        return self.__usuario