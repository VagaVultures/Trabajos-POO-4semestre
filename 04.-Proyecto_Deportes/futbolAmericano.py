from deporte import Deporte

class FutbolAmericano(Deporte):
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_max, tamañoCancha):
        super().__init__(nombre, num_jugadores, duracion_min, puntuacion_max)

        self.tamañoCancha = tamañoCancha 

    def forma_de_anotar (self):
        if self.get_puntuacion_max() == 1:
            return "Se anoto un tiro PAT, la pelota atraveso los postes amarillos."
        elif self.get_puntuacion_max() == 2:
            return "Se anoto un Safety, el Quarterback fue tackleado."
        elif self.get_puntuacion_max() == 6:
            return "Se anoto un Touch Down, el jugador llego a la base enemiga."
        else:
            return "Tiro invalidado"

    def tamaño_cancha(self):
        return self.tamañoCancha
    
    #Anotaciones: 
# (Futbol) Punto por gol: 1 punto
# (Americano) Punto por Touchdown: 6 puntos,
# 1 punto patear el balon, safety 2 puntos 
# (Basquetbol) Lanzamiento desde la linea 3 puntos
# Cualquier canasta 2 puntos, tiros libres 1 punto#