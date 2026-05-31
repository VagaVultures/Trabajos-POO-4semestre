#vaca.py

from animales import Animal


class Vaca (Animal):
    def __init__(self, animal, pelaje, nombre, hablar, litrosLeche):
    
        super().__init__(animal, pelaje, nombre, hablar)
            
        self.__litrosLeche = 0


    def reporteProduccion(self):
        if self.__litrosLeche <21:
            print("Produciendo leche")
            self.__litrosLeche += 1
            print(f"Reporte lacteo: {self.__litrosLeche} litro(s) producido(s).")
        else:
            print(f"{self.obtener_nombre()} alcanzo su limite maximo.")
