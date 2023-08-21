from crearProducto import Fruta
from leerArchivo import leerArchivoEntrada

#leyendo el archivo.mov
#realizara modificaciones en la lista de objetos
def leerArchivoMOV(listaPrueba):
    ruta = input('Ingrese la ruta del archivo ".mov": ')
    if ruta.endswith('.mov'):
        with open(ruta, 'r+') as archivo:
            lineas = archivo.readlines()
            #print(lineas)
        #para saber las posiciones de los objetos en la lista
        for i in lineas:
            #print('este es el valor de i antes de modificarlo', i)
            i = i.replace(' ', ';').replace('\n', '').split(';')
            #print(len(i)) #ver el formato final

            #Bandera para saber si hay un producto igual en la ubicación correcta
            productoEncontrado = False
            #Agregamos Cantidad
            if i[0] == 'agregar_stock':
                print('\nRealizando la instrucción: ', i[0])
                for j in range(len(listaPrueba)):
                    #print('--Estamos comparando estos datos: ', listaPrueba[j].nombre, '|', i[1])
                    #Nombre del producto de la primera linea comparado con todos los objetos
                    if listaPrueba[j].nombre == i[1] and listaPrueba[j].ubi == i[3]:
                        print('--- cantidad registrada: ',listaPrueba[j].cantidad )
                        print(f'Cantidad de {i[1]} para agregar: ', i[2])
                        #actualizando
                        listaPrueba[j].cantidad = int(listaPrueba[j].cantidad) + int(i[2])
                        print('--- cantidad nueva: ',listaPrueba[j].cantidad )
                        productoEncontrado = True
                        break
                #El producto no se encontro
                if productoEncontrado == False:
                    print(f"ERROR: El producto {i[1]} NO EXISTE en la ubicación {i[3]}")

            #Eliminamos cantidad
            elif i[0] == 'vender_producto':
                print('\nRealizando la instrucción: ', i[0])
                for j in range(len(listaPrueba)):
                    #print('--Estamos comparando estos datos: ', listaPrueba[j].nombre, '|', i[1])
                    #Nombre del producto de la primera linea comparado con todos los objetos
                    if listaPrueba[j].nombre == i[1] and listaPrueba[j].ubi == i[3]:
                        print('--- cantidad registrada: ',listaPrueba[j].cantidad )
                        tempCantidad = int(listaPrueba[j].cantidad) - int(i[2])
                        #Para no tener numero negativos
                        if tempCantidad < 0:
                            print(f'Cantidad de {i[1]} para vender: ', i[2])
                            print(f'ERROR: en {i[3]} no hay suficiente stock de inventario para {i[1]}')
                        else:
                            print(f'Cantidad de {i[1]} para vender: ', i[2])
                            listaPrueba[j].cantidad = tempCantidad
                            print('--- cantidad nueva: ',listaPrueba[j].cantidad )
                        productoEncontrado = True
                        break
                #el producton no se encontro
                if productoEncontrado == False:
                    print(f"ERROR: El producto {i[1]} NO EXISTE en la ubicación {i[3]}")

            #Si hay alguna instrucción no reconocida
            else:
                print('\nRealizando la instrucción: ', i[0])
                print('La acción no es compatible')
        
        print('\nSe han ACTUALIZADO los datos en el inventario de forma exitosa')
        input('Presione ENTER para continuar ')
    else:
        print('Debe ingresar un archivo ".mov"')
        input('Presione enter para continuar: ')

#prueba
'''
listaPrueba = []
leerArchivoEntrada(listaPrueba)
leerArchivoMOV(listaPrueba)
'''