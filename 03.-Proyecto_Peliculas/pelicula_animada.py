from pelicula import Pelicula

class PeliculaAnimada(Pelicula):
    def __init__(self, titulo, director, duracion, puntuacion, anio, publico):
        super().__init__(titulo, director, duracion, puntuacion, anio)
        self.publico = publico

    def obtener_clasificacion(self):
        return "AA — apta para toda la familia"
