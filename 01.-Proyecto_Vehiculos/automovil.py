#automovil.py

from vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca: str, modelo: str, anyo: int, numeroPuertas: int, tipoTransmision: str):
        #llamamos al constructor de la clase padre(Vehiculo)
        
        super().__init__(marca, modelo, anyo)

        #atributos especificos del automovil.
        self.__numeroPuertas = numeroPuertas
        self.__tipoTransmision = tipoTransmision

    def abrirMaletero(self):
        print(f"Abriendo el maletero del auto {self.obtenerInformacion()}....")

    def ActivarAireAcondicionado(self):
        print(f"Aire acondicionado acivado; que fresco!")