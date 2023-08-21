from leerArchivo import leerArchivoEntrada
from leerArchivoMOV import leerArchivoMOV
from informeInventario import escribirTXT

#main principal
def menu():
    listaPrincipal = []
    menu = True
    while(menu):
        print('\n')
        print('*'*47)
        print('Práctica 1 - Lenguajes Formales de Programación')
        print('*'*47,'\n')
        print('# SISTEMA DE INVENTARIO\n')
        print('''1. Cargar Inventario Inicial
2. Cargar instrucción de Movimiento
3. Crear Infome de Inventario
4. Salir\n''')
        op = input('Ingrese una opción: ')
        if op == '1':
            print('\n---> 1. Cargar Inventario Inicial')
            #llamos a la funcion que lee el archivo.inv y almacena en la listaPrincipal
            leerArchivoEntrada(listaPrincipal)
            
        elif op == '2':
            print('\n---> 2. Cargar instrucción de Movimiento\n')
            if not listaPrincipal:
                print('Debe cargar primero el INVENTARIO INICIAL\n')
                input('Presione ENTER para continuar ')
            else:
                leerArchivoMOV(listaPrincipal)
        elif op == '3':
            print('\n---> 3. Crear Infome de Inventario\n')
            if not listaPrincipal:
                print('Debe cargar primero el INVENTARIO INICIAL\n')
                input('Presione ENTER para continuar ')
            else:
                escribirTXT(listaPrincipal)
        elif op == '4':
            menu = False
            print('Cerrando el programa...\n')
        else:
            print('Ingrese una opción valida')
            input('Presione ENTER para continuar ')
            #menu() -> con recursividad 
    print('-'*80,'\n')

menu()
