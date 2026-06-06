from pelicula import Pelicula
from pelicula_accion import PeliculaAccion
from pelicula_animada import PeliculaAnimada
from pelicula_documental import PeliculaDocumental

def main():
    p1 = Pelicula("Titanic", "James Cameron", 194, 6, 1997)
    pa = PeliculaAccion("John Wick", "Chad Stahelski", 101, 8, 2014, "alta")
    an = PeliculaAnimada("El rey león", "Roger Allers", 88, 9, 1994, "familiar")
    doc = PeliculaDocumental("Nuestro planeta", "Alastair Fothergill", 50, 9, 2019, "naturaleza")

    peliculas = [p1, pa, an, doc]

    for p in peliculas:
        p.mostrar_info()
        print("¿Es larga?", p.es_larga())
        print("Clasificación:", p.obtener_clasificacion())
        print("-" * 40)

if __name__ == "__main__":
    main()