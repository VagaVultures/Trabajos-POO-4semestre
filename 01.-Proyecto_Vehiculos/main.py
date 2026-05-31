#main.py #recuerda hacer el from e import de cada clase
from motocicleta import Motocicleta
from automovil import Automovil
from camion import Camion

def main():
    print(" || - - - Creando Instancias - - - ||")
    #instanciamos el objeto
    mi_auto = Automovil ("Toyota", "Corolla", 2024, 4, "Automatica")
    mi_moto = Motocicleta ("Harley Davidson", "Softail", 2014, 1450, "si", bool)
    mi_camion = Camion ("Kenworth", "T680", 2022, 40, 3, float)

    print("\n || - - - Probando Metodos de mi auto - - - ||")
    print(mi_auto.obtenerInformacion())
    print(mi_auto.acelerar())
    print(mi_auto.frenar())
    print(mi_auto.abrirMaletero())
    print(mi_auto.ActivarAireAcondicionado())

    print("\n || - - - Probando Metodos de mi moto - - - ||")
    print(mi_moto.obtenerInformacion())
    print(mi_moto.acelerar())
    print(mi_moto.frenar())
    print(mi_moto.bajarCaballete())
    print(mi_moto.subirCaballete())
    print(mi_moto.levantarCaballito())

    print("\n || - - - Probando Metodos de mi camion - - - ||")
    print(mi_camion.obtenerInformacion())
    print(mi_camion.acelerar())
    print(mi_camion.frenar())
    print(mi_camion.cargar())
    print(mi_camion.descargar())


if __name__ == "__main__":
    main()


