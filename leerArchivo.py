from crearProducto import Fruta

#METODO PARA MOSTRAR LOS VALORES DE UNA LISTA
def mostrar(lista):
    k= 0
    while k < len(lista):
        #leer los datos de la lista a través de sus atributos
        #print(lista[k].nombre,' ', lista[k].cantidad,' ', lista[k].precio,' ', lista[k].ubi )
        lista[k].mostrarInfo()
        k+=1

#Leer el archio.inv por linea y lo mete en una lista de objetos
def leerArchivoEntrada(listaFrutas):
    #listaFrutas = []
    #SELECCIONAR EL Archivo.inv
    ruta = input('Escriba la ruta del archivo ".inv": ')

    #Abre le archivo y lo cierra posteriormente
    #lee linea x linea
    with open(ruta,'r') as archivo:
        #archivo = open(ruta, 'r+') -> abre le archivo pero no lo cierra
        lineas = archivo.readlines()
        #imprime una lista y los valores son las lineas
        #print(lineas)

    #leyendo linea por linea y remplazando
    for i in lineas:
        #lee por linea y remplaza lo devido
        i = i.replace('crear_producto ','').replace('\n','').split(';')
        #i.split(';')
        
        contador = 1
        tempNombre = None
        tempCantidad = None
        tempPrecio = None
        tempUbi = None
        for j in i:
            if contador ==1:
                tempNombre = j
            elif contador == 2:
                tempCantidad = j
            elif contador == 3:
                tempPrecio = j
            elif contador == 4:
                tempUbi = j
            contador += 1
        miFruta = Fruta(tempNombre, tempCantidad, tempPrecio, tempUbi)
        listaFrutas.append(miFruta)

        mostrar(listaFrutas)
        #print(i)
        #la final de cada linea ha un '\n' entoces corta pero el '\n' aun se ejecuta
        #i.split('\n')

        #lee por linea sin los []
        #print(i.replace('\n', ''))
        

#Se llama a la función para hacer pruebas en este archivo.py
#leerArchivoEntrada()

#C:/Users/gio/Desktop/LAB_LFP_2s23/Practica1/prueba.inv 1:21:47