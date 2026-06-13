from gato import Gato
from gallina import Gallina
from perro import Perro
from gestor_datos import GestorJSON

def main():
    # 1. Instanciamos el objeto en la memoria RAM
    mi_gato01 = Gato("Garfield", 5, "Naranja")
    mi_gato02 = Gato("Maldad", 4, "Negro")
    mi_gallina01 =  Gallina("Turuleca", 2, 3)
    mi_gallina02 = Gallina("Pintadita", 5, 1)
    mi_perro01 = Perro("Sif", 1600, 0, "Gris")
    mi_perro02 = Perro("Maylo", 13, 74, "Atigrado")

    # 2. Preparamos las estructuras de datos limpias
    lista_animales = [mi_gato01, mi_gato02, mi_gallina01, mi_gallina02, mi_perro01, mi_perro02]
    datos_a_guardar = []
    
    # 3. Ciclo de transformación (Serialización de objetos a diccionarios)
    for animal in lista_animales:
        datos_a_guardar.append(animal.convertir_a_diccionario())

    # 4. Delegamos la persistencia física al gestor especializado
    base_datos = GestorJSON()
    base_datos.guardar_datos(datos_a_guardar)

if __name__ == "__main__":
    main()
