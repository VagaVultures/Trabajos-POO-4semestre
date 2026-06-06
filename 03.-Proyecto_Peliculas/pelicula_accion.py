from pelicula import Pelicula

class PeliculaAccion(Pelicula):
    def __init__(self, titulo, director, duracion, puntuacion, anio, nivel_accion):
        super().__init__(titulo, director, duracion, puntuacion, anio)
        self.nivel_accion = nivel_accion

    def obtener_clasificacion(self):
        return "B15 — no recomendada para menores de 15 años"