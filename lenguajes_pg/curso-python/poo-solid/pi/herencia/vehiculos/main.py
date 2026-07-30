from moto import Moto
from furgoneta import Furgoneta
from bicicleta_electrica import BicicletaElectrica

# Instanciar una moto
mi_moto = Moto("Honda", "CBR")

mi_moto.caballito()
mi_moto.estado()

print()

# Instanciar una furgoneta
furgoneta = Furgoneta("Renault", "Kangoo")

furgoneta.arranchar()
furgoneta.estado()

print(furgoneta.carga(True), end="\n\n")

# Instanciar una bicicleta eléctrica que maneja múltiple herencia
bicicleta_electrica = BicicletaElectrica("Xiaomi", "Qicycle")
bicicleta_electrica.estado()