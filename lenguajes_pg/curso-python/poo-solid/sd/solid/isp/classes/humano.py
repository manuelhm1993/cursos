from ..interfaces.itrabajador import ITrabajador
from ..interfaces.idurmiente import IDurmiente
from ..interfaces.icomedor import IComedor

class Humano(ITrabajador, IDurmiente, IComedor):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")