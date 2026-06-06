from deporte import Deporte

class Futbol(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_max, arbitros):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_max)

        self.arbitros = arbitros 

    def forma_de_anotar(self):
        return "El balon entro a la porteria, se anoto un Gol"
    
    def arbitros_en_partido(self):
        return self.arbitros
    
