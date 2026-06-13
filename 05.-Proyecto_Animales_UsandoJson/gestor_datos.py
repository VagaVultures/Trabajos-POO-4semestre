import json
import os

class GestorJSON:
    def __init__(self, nombre_archivo="granja.json"):
        # Localiza dinámicamente el directorio del script para evitar archivos perdidos en VS Code
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        self.__ruta_completa = os.path.join(directorio_actual, nombre_archivo)

    def guardar_datos(self, lista_diccionarios: list):
        try:
            # Abre o crea el archivo en modo escritura pura ('w')
            with open(self.__ruta_completa, 'w', encoding='utf-8') as archivo:
                json.dump(lista_diccionarios, archivo, indent=4, ensure_ascii=False)
            
            print(f"Éxito: Datos guardados correctamente.")
            print(f"Ubicación del archivo: {self.__ruta_completa}")
            
        except IOError as error:
            print(f"Error crítico al intentar escribir en el disco duro: {error}")
        
    def cargar_datos(self) -> list:
        #Busca el archivo JSON en el disco duro, valida su existencia y lo taduce a una
        # lista de diccionarios Python.

        #1 regla del clean code, Validar si el archivo NO existe antes de abrirlo.

        if not os.path.exists(self.__ruta_completa):
            print(f"Aviso, el archivo {self.__ruta_completa} no existe. Se devolvera una lista vacia.")
            return []
        
        #2 intenta leer el archivo de forma segura

        try:
            #'r' significa modo de lectura (Read)
            with open (self.__ruta_completa, 'r', encoding='utf-8') as archivo:
                    #json.load toma el texto plano del archivo y lo convierte en estructuras de Python (Listas/diccionarios).
                    datos_recuperados = json.load(archivo)
                    return datos_recuperados
        except json.JSONDecodeError:
            #se ejecuta si el archivo el archivo existe pero esta totalmente vacio o corrupto
            print ("Error: El archivo JSON esta corrupto o mal estructurado.")
            return []

