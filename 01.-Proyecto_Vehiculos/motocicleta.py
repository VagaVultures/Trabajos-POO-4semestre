from vehiculo import Vehiculo



class Motocicleta(Vehiculo):
    def __init__(self, marca: str, modelo: str, anyo:int, cilindrada: int, caballete: str, patita: bool):
        super().__init__(marca, modelo, anyo)
        
        self.__patita = False


        #atributos de la moto
        self.__cilindrada = cilindrada
        self.__caballete = caballete

    def levantarCaballito(self):
        print(f"Haciendo un caballito en la moto...")
    
    def bajarCaballete(self):
        print(f"Bajando el caballete de la moto...")
        if self.__patita == False:
            self.__caballete = "Abajo"
  
            print(f"Caballete {self.__caballete}")
            self.__patita = True
        else:
            print(f"El caballete ya esta abajo")

    def subirCaballete(self):
        print(f"Subiendo el caballete de la moto...")
        if self.__patita == True:
            self.__caballete = "Arriba"
  
            print(f"Caballete {self.__caballete}")
            self.__patita = False
        else:
            print(f"El caballete ya esta arriba.")

