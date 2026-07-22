from ..interfaces.itrabajador import ITrabajador

class Robot(ITrabajador):
    def trabajar(self):
        print("El robot está trabajando")