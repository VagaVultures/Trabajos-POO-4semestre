from pelicula import Pelicula

class PeliculaDocumental(Pelicula):
    def __init__(self, titulo, director, duracion, puntuacion, anio, tematica):
        super().__init__(titulo, director, duracion, puntuacion, anio)
        self.tematica = tematica

    def obtener_clasificacion(self):
        return "TVPG — Guia paternal sugerida"
