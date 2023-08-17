#CLASE PARA CARGAR INVENTARIO INICIAL
class Fruta():
    def __init__(self, nombre, cantidad, precio, ubi):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.ubi = ubi

    def mostrarInfo(self):
        print('\n----------------')
        print('Fruta: ', self.nombre)
        print('Cantidad: ', str(self.cantidad))
        print('Precio Unitario: ' + str(self.precio))
        print('Ubicación: ' + self.ubi +'\n----------------\n')


'''
#EN ESTA LISTA SE GUARDAN TODOS LOS OBJETOS
lista=[]

#METODO PARA MOSTRAR LOS VALORES DE UNA LISTA
def mostrar():
    k= 0
    while k < len(lista):
        #leer los datos de la lista
        #print(lista[k].nombre,' ', lista[k].cantidad,' ', lista[k].precio,' ', lista[k].ubi )
        lista[k].mostrarInfo()
        k+=1

#PRUEBA PARA INGRESAR VALORES A UN OBJETO 
salirMenu = True
while (salirMenu):
    print('\n1.Agregar fruta\n2.Mostrar frutas\n3.salir\n')
    op = input('seleccion: ')
    if op == '1':
        print('\nregistrar ***')
        nom = str(input('nombre: '))
        can = int(input('Cantidad: '))
        prec = float(input('Precio unitario: '))
        ubi = str(input('Ubicación: '))

        miFruta = Fruta(nom, can, prec, ubi)
        lista .append(miFruta)
        print('Fruta registrada con éxito')

    if op == '2':
        print('\n mostrar ***')
        mostrar()
    if op == '3':
        salirMenu = False
        print('salir')
'''