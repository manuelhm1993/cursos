class Usuario:
    def __init__(self, nombre: str, email: str, telefono_sms: str, telefono_whatsapp: str) -> None:
        self.__nombre            = nombre
        self.__email             = email
        self.__telefono_sms      = telefono_sms
        self.__telefono_whatsapp = telefono_whatsapp

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def telefono(self) -> str:
        return self.__telefono_sms

    @property
    def email(self) -> str:
        return self.__email

    @property
    def whatsapp(self) -> str:
        return self.__telefono_whatsapp