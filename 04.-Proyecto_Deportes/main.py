from deporte import Deporte
from futbol import Futbol
from basquetbol import Basquetbol
from futbolAmericano import FutbolAmericano

def main():
#self, nombre, num_jugadores, duracion_min, puntuacion_max, num_arbitros
    fut = Futbol("Futbol", 22, 90, 1, 4)
    bas = Basquetbol("Basquetbol", 10, 120, 3, 3.5)
    ame = FutbolAmericano("Futbol Americano", 22, 60, 6, 100)

    fut.mostrar_info()
    print(fut.forma_de_anotar())
    print(f"Hay",fut.arbitros_en_partido(),"arbitros en el partido")
    print("-" * 40)
    
    bas.mostrar_info()
    print(bas.forma_de_anotar())
    print(f"La canasta esta a",bas.altura_canasta(),"mts de altura")
    print("-" * 40)
    
    ame.mostrar_info()
    print(ame.forma_de_anotar())
    print(f"La cancha tiene",ame.tamaño_cancha(),"yardas para ser recorridas")
    print("-" * 40)
    
if __name__ == "__main__":
    main()