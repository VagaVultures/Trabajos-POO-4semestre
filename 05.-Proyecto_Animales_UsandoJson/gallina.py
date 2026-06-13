#gallina.py

from animal import Animal


class Gallina (Animal):
    def __init__(self, nombre:str, edad:int, ponerHuevo:int):
        super().__init__(nombre, edad)

        self.__ponerHuevo = ponerHuevo

    def huevo(self):
        print("Poniendo un huevo")
        
        self.__ponerHuevo += 1

        print(f"Huevos puestos: {self.__ponerHuevo}")
    
    def hablar(self):
        print("¡Pock-Pock!")

    def convertir_a_diccionario(self) -> dict:
        return{
            "especie":"Gallina",
            "nombre":self.obtener_nombre(),
            "edad":self.obtener_edad(),
            "Huevo_Producido":self.__ponerHuevo
        }