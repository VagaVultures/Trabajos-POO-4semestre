class Deporte:
    def __init__(self, nombre, num_jugadores, duracion_min, puntuacion_max):
        self.nombre       = nombre
        self.num_jugadores     = num_jugadores
        self.duracion_min     = duracion_min
        self.__puntuacion_max = puntuacion_max   # atributo privado

    def mostrar_info(self):
        print("Nombre:                  ", self.nombre)
        print("Jugadores en el campo:   ", self.num_jugadores)
        print("Duración:                ", self.duracion_min, "minutos")
        print("Puntuación:              ", self.__puntuacion_max)


    def get_puntuacion_max(self):
        return self.__puntuacion_max