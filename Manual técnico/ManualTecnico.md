# Lenguajes Formales de Programación
## Práctica 1
### 2do Semestre 2023

```js
Universidad San Carlos de Guatemala
Programador: Giovanni Saul Concohá
Carne: 202100229
Correo: --
```
---
## Descripción del Proyecto
Los estudiantes serán desafiados a crear un programa en el lenguaje de programación Python que tenga la capacidad de administrar un inventario, además de rastrear y documentar los cambios que ocurren en la existencia de productos mediante el uso de archivos de texto.

## Objetivos
* Objetivo General
    * Aprender a utilizar archivos.
* Objetivos Específicos
    * Inplementar una solución de software con base en los distintos paradigmas de programación vistos en clase y laboratorio.
    * Adquirir habilidades en el manejo de archivos, lógica de programación y manipulación de estructuras de datos en Python.

---
## Archivos .py 
### CrearProducto.py

esta clase se utiliza para modelar las características y propiedades de las frutas en el inventario. La lógica se basa en la encapsulación de datos, ya que cada fruta se representa como un objeto independiente con sus atributos únicos. La información se almacena en instancias de la clase "Fruta", lo que permite una representación ordenada y coherente de los datos del inventario.
La clase tiene un constructor (__init__) que acepta cuatro parámetros: "nombre", "cantidad", "precio" y "ubi" (ubicación). Estos parámetros se utilizan para inicializar las propiedades de cada objeto de fruta.

La clase "Fruta" tiene dos métodos:

'__init__(self, nombre, cantidad, precio, ubi)': Este es el constructor de la clase. Se encarga de inicializar las propiedades del objeto fruta cuando se crea una instancia de la clase. Los parámetros proporcionados son asignados a las variables de instancia correspondientes (self.nombre, self.cantidad, self.precio y self.ubi).

'mostrarInfo(self)': Este método se utiliza para mostrar la información de la fruta en la consola. Imprime el nombre de la fruta, la cantidad disponible, el precio unitario y la ubicación. La información se presenta de manera organizada con un formato específico.

## leerArchivo.py
Este archivo se encarga de leer un archivo ".inv" que contiene información sobre productos (frutas), extraer los datos necesarios de cada línea, y crear objetos Fruta con esos datos. Los objetos Fruta se almacenan en la lista listaFrutas, que puede ser utilizada posteriormente en el programa para gestionar el inventario y los movimientos de productos.

## leerArchivoMOV.py
En esencia, este código procesa un archivo ".mov" que contiene instrucciones para agregar o vender productos en el inventario representado por la lista de objetos Fruta. Las cantidades de los productos se actualizan según las instrucciones del archivo ".mov".

Al final del proceso, después de procesar todas las líneas del archivo ".mov", se muestra un mensaje que confirma la exitosa actualización de los datos en el inventario. Esto significa que la lista de objetos Fruta ha sido modificada según las instrucciones proporcionadas en el archivo ".mov".

## informeInventario.py
Este archivo toma una lista de objetos Fruta, calcula el valor total para cada producto y crea un informe de inventario en formato de archivo de texto. La presentación de los datos en el archivo es organizada y legible, con encabezados y líneas de separación que ayudan a visualizar los detalles de los productos y sus valores totales.

En resumen, el archivo de texto 'resultado_202100229.txt' contendrá un informe estructurado que incluirá los nombres, cantidades, precios unitarios, valores totales y ubicaciones de los productos presentes en la lista listaProductos. Cada producto se presentará en una línea, con columnas alineadas y un encabezado que indica el propósito del informe.

## menu.py
Este archivo representa el flujo principal del programa, permitiendo al usuario realizar diversas acciones relacionadas con la gestión del inventario, como cargar inventario inicial, actualizarlo con instrucciones de movimiento y generar informes de inventario. Cada acción es manejada por una función específica, lo que proporciona una estructura organizada y funcional al sistema de inventario.

