#automovil.py

from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca: str, modelo: str, anyo: int, capacidadCarga: float, numeroEjes: int, cargaActual: float):
        #llamamos al constructor de la clase padre(Vehiculo)
        
        self.__cargaActual = 40

        super().__init__(marca, modelo, anyo)

        #atributos especificos del camion.
        self.__capacidadCarga = capacidadCarga
        self.__numeroEjes = numeroEjes

    def cargar(self):
        print(f"Cargando en el camion...")
        if self.__cargaActual < 40:
            self.__cargaActual += 1
            print(f"Camion cargado con exito!")
            print(f"Carga actual es de {self.__cargaActual} toneladas")
        else:
            print(f"Carga maxima alcanzada.")
            



    def descargar(self):
        print(f"Descargando el camion...")
        if self.__cargaActual > 0:
            self.__cargaActual -= 1
            print(f"Carga actual es de {self.__cargaActual} toneladas")
            print(f"Camion descargado con exito!")
        else:
            print(f"Camion completamente vaciado.")
            

    