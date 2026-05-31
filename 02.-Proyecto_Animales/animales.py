#animales.py

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, animal, pelaje, nombre, hablar):
        self.__animal = animal
        self.__nombre = nombre
        self.__pelaje = pelaje
        self.__hablar = hablar

    def hablar(self):
        return print(self.__hablar)

    def obtener_nombre(self):
        return self.__nombre

    def obtenerDatos(self) -> str:
        if self.__animal == 'Gallina':
            return f"Animal {self.__animal} de plumaje {self.__pelaje} y nombre {self.__nombre}."
        else:
            return f"Animal {self.__animal} de pelaje {self.__pelaje} y nombre {self.__nombre}."

