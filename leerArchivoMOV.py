

def leerArchivoMOV():
    ruta = input('Ingrese la ruta del archivo ".mov": ')
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        #print(lineas)

    for i in lineas:
        print('este es el valor de i antes de modificarlo', i)
        i = i.replace(' ', ';').replace('\n', '').split(';')
        #print(len(i))
        #print('antes de recorrec cada linea', i[0])

        if i[0] == 'agregar_stock':
            print(i[0])
            pass
        elif i[0] == 'vender_producto':
            print(i[0])
            pass
        else:
            print('no es comopatible')
        '''for j in i:
            #j es el 1er valor en la lista i
            #i es la lista deparada por ; de cada linea
            if j == 'agregar_stock':
                print(j)
                break
            elif j == 'vender_producto':
                print(j)
                break
            else:
                print('no es compatible')
                break
'''
        
        #print(i)

leerArchivoMOV()