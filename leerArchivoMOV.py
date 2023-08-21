from crearProducto import Fruta
from leerArchivo import leerArchivoEntrada
#leyendo el archivo.mov
#realizara modificaciones en la lista de objetos


def leerArchivoMOV(listaPrueba):
    ruta = input('Ingrese la ruta del archivo ".mov": ')
    with open(ruta, 'r+') as archivo:
        lineas = archivo.readlines()
        #print(lineas)
    #para saber las posiciones de los objetos en la lista
    for i in lineas:
        #print('este es el valor de i antes de modificarlo', i)
        i = i.replace(' ', ';').replace('\n', '').split(';')
        #print(len(i))
        #print('antes de recorrec cada linea', i[0])

        #Bandera para saber si hay un producto igual en la ubicación correcta
        productoEncontrado = False
        #Agregamos Cantidad
        if i[0] == 'agregar_stock':
            print('Estamos haciendo esta instruccion ', i[0])
            for j in range(len(listaPrueba)):
                print('--Estamos comparando estos datos: ', listaPrueba[j].nombre, '|', i[1])
                #Nombre del producto de la primera linea comparado con todos los objetos
                if listaPrueba[j].nombre == i[1] and listaPrueba[j].ubi == i[3]:
                    print('--- cantidad actual:',listaPrueba[j].cantidad )
                    listaPrueba[j].cantidad = int(listaPrueba[j].cantidad) + int(i[2])
                    print('--- cantidad nueva:',listaPrueba[j].cantidad )
                    productoEncontrado = True
                    break
            if productoEncontrado == False:
                print(f"ERROR: El producto {i[1]} NO EXISTE en la ubicación {i[3]}")

        #Eliminamos cantidad
        elif i[0] == 'vender_producto':
            print('Estamos haciendo esta instruccion ', i[0])
            for j in range(len(listaPrueba)):
                print('--Estamos comparando estos datos: ', listaPrueba[j].nombre, '|', i[1])
                #Nombre del producto de la primera linea comparado con todos los objetos
                if listaPrueba[j].nombre == i[1] and listaPrueba[j].ubi == i[3]:
                    print('--- cantidad actual:',listaPrueba[j].cantidad )
                    tempCantidad = int(listaPrueba[j].cantidad) - int(i[2])
                    if tempCantidad < 0:
                        print(f'ERROR: en {i[3]} no hay suficiente stock de inventario para {i[1]}')
                    else:
                        listaPrueba[j].cantidad = tempCantidad
                        print('--- cantidad nueva:',listaPrueba[j].cantidad )
                    productoEncontrado = True
                    break
            if productoEncontrado == False:
                print(f"ERROR: El producto {i[1]} NO EXISTE en la ubicación {i[3]}")

        #Si hay alguna instrucción no reconocida
        else:
            print('Estamos haciendo esta instrucción ', i[0])
            print('La acción no es compatible')

listaPrueba = []
leerArchivoEntrada(listaPrueba)
leerArchivoMOV(listaPrueba)