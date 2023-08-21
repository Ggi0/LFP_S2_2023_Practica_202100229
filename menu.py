from leerArchivo import leerArchivoEntrada
from informeInventario import escribirTXT

#en esta lista es almacenaran todos los objetos.

def menu():
    listaPrincipal = []
    menu = True
    while(menu):
        print('*'*50)
        print('Práctica 1 - Lenguajes Formales de Programación')
        print('*'*50,'\n')
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
            print('La carga inicial fue agregada exitosamente')
            input('Presione ENTER para continuar ')
        elif op == '2':
            print('\n---> 2. Cargar instrucción de Movimiento\n')
            if not listaPrincipal:
                print('Debe cargar primero el INVENTARIO INICIAL\n')
                input('Presione ENTER para continuar ')
        
        elif op == '3':
            print('\n---> 3. Crear Infome de Inventario\n')
            if not listaPrincipal:
                print('Debe cargar primero el INVENTARIO INICIAL\n')
                input('Presione ENTER para continuar ')
            else:
                escribirTXT(listaPrincipal)
                print('El Informe de Inventario fue generado exitosamente')
                input('Presione ENTER para continuar ')
        
        elif op == '4':
            menu = False
            print('Cerrando el programa...\n')
        else:
            print('Ingrese una opción valida')
            input('Presione ENTER para continuar ')
            #menu() -> con recursividad 

    print('-'*80,'\n')

menu()
