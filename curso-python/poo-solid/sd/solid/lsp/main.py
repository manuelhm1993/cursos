"""LSP: Principio de sustitución de Liskov, dicta que las clases derivadas tienen que
ser sustituibles por sus clases padre. A -> B. A puede utilizarse en todos los lugares
que B puede ser utilizada"""
from .ave import AveVoladora, Pinguino

def hacer_volar(ave: AveVoladora) -> str:
    print(ave.volar())

"""Si se quiere crear una clase pingüino, este tipo de ave no puede volar, eso significa
que no cumple el principio lsp, entonces se crea una jerarquía: Ave -> (AveVoladora && AveNoVoladora)
Para poder entonces crear la clase Pinguino que no puede usar el método volar"""
ave      = AveVoladora()
pinguino = Pinguino()

hacer_volar(ave)