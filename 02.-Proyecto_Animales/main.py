
from gato import Gato
from gallina import Gallina
from vaca import Vaca

def main():
    print("Instanciando.................")

    mi_gato = Gato("Gato", "Naranja", "Jibanyan", "Meow :3",str)
    print("Metodos felinos")
    print(mi_gato.obtenerDatos())
    print("El gato hace: ", end=" ")
    mi_gato.hablar()
    mi_gato.purr()
    mi_gato.Un_purr()
    print("\r")

    mi_gallina = Gallina("Gallina", "Blanco", "Turuleca", "Pock-Pock :^", int)
    print("Metodos aviarios") 
    print(mi_gallina.obtenerDatos())
    print("La gallina hace: ",end=" ")
    mi_gallina.hablar()
    mi_gallina.huevo() 
    print("\r")

    mi_vaca = Vaca("Vaca", "Blanco", "Conquest", "Mooo (I am... so lonely, i dont even have a name, just a purpose).", int)
    print("Metodos bovinos")
    print(mi_vaca.obtenerDatos())
    print("La vaca hace: ",end=" ")
    mi_vaca.hablar()
    mi_vaca.reporteProduccion()
    print("\r")
    


if __name__ == "__main__":
    main()

