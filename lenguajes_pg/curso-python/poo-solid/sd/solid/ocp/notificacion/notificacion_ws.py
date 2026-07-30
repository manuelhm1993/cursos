from .notificacion import Notificacion
from ..usuario import Usuario

class NotificacionWS(Notificacion):
    def __init__(self, usuario: Usuario, mensaje: str) -> None:
        super().__init__(usuario, mensaje)

    def notificar(self) -> None:
        print(f"Mensaje enviado al whatsApp: {self.usuario.whatsapp}")