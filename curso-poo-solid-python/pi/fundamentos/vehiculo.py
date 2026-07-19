# Primera clase
class Vehiculo:
    # Propiedad de clase private static
    __id = 0

    # Método constructor para definir propiedades de clase. La propiedad self equivale a this, pero es obligatoria en python
    def __init__(self):
        Vehiculo.__id += 1

        # Para encapsular una propiedad se usa el __ antes del nombre, equivale a private
        self.__largo_chasis = 250
        self.__ancho_chasis = 120
        self.__ruedas       = 4
        self.__en_marcha    = False
        self.__id           = Vehiculo.__id
    
    # Método para arrancar el vehículo y ver su estádo, es un getter y setter (no recomendable)
    def arrancar(self, arranque: bool) -> str:
        if arranque:
            chequeo = self.__chequeo_interno()
            self.__en_marcha = chequeo
        else:
            self.__en_marcha = arranque

        if arranque and chequeo:
            estatus = f"El vehículo {self.__id} está encendido"
        elif arranque and not chequeo:
            estatus = f"El chequeo interno falló, el vehículo {self.__id} está apagado"
        else:
            estatus = f"El vehículo {self.__id} está apagado"

        return estatus
    
    # Método getter para obtener las características del vehículo
    def estado_vehiculo(self) -> None:
        print(f"""Propiedades del vehículo {self.__id}
- Longitud: {self.__largo_chasis}cm
- Ancho: {self.__ancho_chasis}cm
- Número de ruedas: {self.__ruedas}""")
    
    # Método encapsulado
    def __chequeo_interno(self) -> bool:
        print("Realizando chequeo interno")

        self.__gasolina = "ok"
        self.__aceite   = "ok"
        self.__puertas  = "cerradas"

        return self.__gasolina == "ok" and self.__aceite == "ok" and self.__puertas == "cerradas"

# Intanciar una clase o definir un objeto
vehiculo1 = Vehiculo()
vehiculo2 = Vehiculo()

# Usar los comportamientos del objeto
vehiculo1.estado_vehiculo()
print(vehiculo1.arrancar(True))

print()

vehiculo2.estado_vehiculo()
print(vehiculo2.arrancar(False))