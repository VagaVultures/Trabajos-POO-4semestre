class Pelicula:
    def __init__(self, titulo, director, duracion, puntuacion, anio):
        self.titulo       = titulo
        self.director     = director
        self.duracion     = duracion
        self.__puntuacion = puntuacion   # atributo privado
        self.anio         = anio

    def mostrar_info(self):
        print("Título:     ", self.titulo)
        print("Director:   ", self.director)
        print("Duración:   ", self.duracion, "minutos")
        print("Puntuación: ", self.__puntuacion)
        print("Año:        ", self.anio)

    def get_puntuacion(self):
        return self.__puntuacion

    def set_puntuacion(self, valor):
        if 0 <= valor <= 10:
            self.__puntuacion = valor
        else:
            print("Error: la puntuación debe estar entre 0 y 10")

    def es_larga(self):
        return self.duracion > 120
    
    def obtener_clasificacion(self):
        return "AA — apta para toda la familia"