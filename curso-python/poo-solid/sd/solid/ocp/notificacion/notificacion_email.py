from .notificacion import Notificacion
from ..usuario import Usuario

class NotificacionEmail(Notificacion):
    def __init__(self, usuario: Usuario, mensaje: str) -> None:
        super().__init__(usuario, mensaje)

    def notificar(self) -> None:
        print(f"Correo enviado a la dirección: {self.usuario.email}")