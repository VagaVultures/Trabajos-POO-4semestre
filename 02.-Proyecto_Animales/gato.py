#gato.py

from animales import Animal


class Gato (Animal):
    def __init__(self, animal, pelaje, nombre, hablar, ronronear):
    
        super().__init__(animal, pelaje, nombre, hablar)
            
        self.__ronronear = 'silencio'               

        
    def purr(self):
        print("*ronroneando*")
        if self.__ronronear == 'silencio':
            print("purrrrrrrrrrrrrrrrrrrrrrrrr")
            self.__ronronear = 'ruido'
        else:
            print("Ya estoy ronroneando!")
                
    def Un_purr(self):
        print("*desronroneando*")

        if self.__ronronear == 'ruido':
            print(".........")
            self.__ronronear = 'silencio'
            
        else:
            print("Ya estoy en silencio!")
