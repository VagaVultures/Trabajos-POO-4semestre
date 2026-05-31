
#vehiculo.py
from abc import ABC, abstractmethod #(Abstract base classes).

class Vehiculo (ABC):
    def __init__(self, marca: str, modelo: str, anyo: int):
        #los guiones bajos representan el modificador privado (-) del diagrama. (Atributos)
        self.__marca = marca
        self.__modelo = modelo
        self.__anyo = anyo
        self.__velocidadActual = 0.0 #inicia en 0 por defecto.

    #Metodos publicos (+). (Funciones)
    def acelerar(self):
        self.__velocidadActual += 10.0
        print(f"Acelerando... Velocidad actual: {self.__velocidadActual}km/h")

    def frenar(self):
        if self.__velocidadActual >= 10.0:
            self.__velocidadActual -= 10.0
        
        else:
            self.__velocidadActual = 0.0
        print(f"Frenando... Velocidad actual: {self.__velocidadActual}km/h")

    def obtenerInformacion(self) -> str:
        return f"Vehiculo: {self.__marca} {self.__modelo} ({self.__anyo})"