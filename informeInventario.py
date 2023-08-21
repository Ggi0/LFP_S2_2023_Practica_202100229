from crearProducto import Fruta

#Crear el Informe de inventario 
#Salida archivo.txt

#ingresamos como parametro a escribirTXT() una lista con los objetos 'Fruta'
def escribirTXT(listaProductos):
    with open('pruebaInforme.txt','w') as archivo:
        archivo.write('Informe de Inventario:\n\n')
        archivo.write("{:10} {:^10} {:^20} {:^16} {:^16}".format('Producto','Cantidad','PrecioUnitario','ValorTotal','Ubicación') + '\n')
        archivo.write('-'*72 + '\n')
        '''
        #Espacios entre variables de forma manual
        for i in range(len(listaProductos)):
            valorTotal = round((float(listaProductos[i].cantidad) * float(listaProductos[i].precio)),2)
            archivo.write((f"{listaProductos[i].nombre}  {listaProductos[i].cantidad}   {listaProductos[i].precio}   {valorTotal}   {listaProductos[i].ubi} \n"))
            #verificar que estas obteniendo información del objeto
            #print(listaProductos[i].nombre
        '''

        #centradar entre los espacios establecidos
        for i in range(len(listaProductos)):
            valorTotal = round((float(listaProductos[i].cantidad) * float(listaProductos[i].precio)),2)
            archivo.write("{:10} {:^10} {:^20} {:^16} {:^16}".format(listaProductos[i].nombre,listaProductos[i].cantidad,listaProductos[i].precio,valorTotal,listaProductos[i].ubi)+'\n')



