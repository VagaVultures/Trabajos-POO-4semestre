# Sistema de Gestión - Reino Animal (Módulo de Persistencia)

## Propósito del Proyecto
El proposito de esta practica es probar las distintas caracteristicas que destacan en la programacion orientada a objetos, la abstraccion, herencia y el encapsulamiento permitiendonos trasladar los objetos en forma de texto plano.

## Tecnologías Utilizadas
- Lenguaje: Python 3
- Formato de Almacenamiento: JSON (Librería nativa)

## Guía de Instalación y Ejecución
1. Asegúrese de contar con un entorno de ejecución Python 3 instalado.
2. Abra la terminal de comandos directamente en la carpeta raíz del proyecto.
3. Ejecute el archivo: `python main.py`
4. El software generará automáticamente el archivo persistente `granja.json` en este mismo directorio.

## Arquitectura y Buenas Prácticas
* **Principio de Responsabilidad Única (SRP):** 
La lógica de las entidades del Reino Animal se encuentra completamente aislada de los mecanismos de almacenamiento (GestorJSON).
* **Clean Code:**
Se implementaron nombres de métodos explícitos, encapsulamiento riguroso mediante atributos privados y un manejo controlado de errores para evitar cierres inesperados durante la manipulación de archivos del sistema.

z