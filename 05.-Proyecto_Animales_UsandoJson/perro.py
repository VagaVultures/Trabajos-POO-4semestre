#gallina.py

from animal import Animal


class Perro (Animal):
    def __init__(self, nombre:str, edad:int, escarbar_hoyo:int, color_pelaje:str):
        super().__init__(nombre, edad)

        self.color_pelaje = color_pelaje
        self.escarbar_hoyo = escarbar_hoyo

    def huevo(self):
        print("Escarbando en la tierra.....")
        
        self.escarbar_hoyo += 1

        print(f"Diametro del hoyo escarbado(cm): {self.escarbar_hoyo}")
    
    def hablar(self):
        print("¡Barf!")

    def convertir_a_diccionario(self) -> dict:
        return{
            "especie":"Perro",
            "nombre":self.obtener_nombre(),
            "edad":self.obtener_edad(),
            "pelaje":self.color_pelaje,
            "diametro_del_hoyo_escarbado":self.escarbar_hoyo
        }