from deporte import Deporte

class Basquetbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_max, alturaDecanasta):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_max)

        self.alturaDecanasta = alturaDecanasta 

    def forma_de_anotar (self):
        if self.get_puntuacion_max() == 1:
            return "Se anoto un tiro libre"
        elif self.get_puntuacion_max() == 2:
            return "Se anoto un tiro normal"
        elif self.get_puntuacion_max() == 3:
            return "Se anoto un tiro desde la linea de 3 puntos"
        else:
            return "Tiro invalidado"

    def altura_canasta(self):
        return self.alturaDecanasta
    
    