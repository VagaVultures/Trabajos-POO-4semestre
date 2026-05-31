#gallina.py

from animales import Animal


class Gallina (Animal):
    def __init__(self, animal, pelaje, nombre, hablar,ponerHuevo):
    
        super().__init__(animal, pelaje, nombre, hablar)
            
        self.__ponerHuevo = 0


    def huevo(self):
        print("Poniendo un huevo")
        
        self.__ponerHuevo += 1

        print(f"Contador de huevos: {self.__ponerHuevo}")