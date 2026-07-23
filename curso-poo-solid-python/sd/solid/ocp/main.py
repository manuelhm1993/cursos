"""Principio de abierto/cerrado: dicta que las entidades de software como clases,
módulos, funciones tienen que estar abiertas para la extensión, pero cerradas para
la modificación. Se pueden agregar nuevas funcionalidades, pero no modificar su fuente"""
from .usuario import Usuario
from .notificacion import Notificacion, NotificacionEmail, NotificacionSMS, NotificacionWS

usuario = Usuario("Manuel", "manuelhm1993@gmail.com", "+584246827377", "+584246827377")

notificaciones: list[Notificacion] = [
    NotificacionEmail(usuario, "MHenriquez te da la bienvenida"),
    NotificacionSMS(usuario, "MHenriquez te da la bienvenida"),
    NotificacionWS(usuario, "MHenriquez te da la bienvenida")
]

for notificacion in notificaciones:
    notificacion.notificar()