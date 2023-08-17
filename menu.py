from leerArchivo import leerArchivoEntrada

def menu():
    menu = True
    while(menu):
        print('\n','*'*50)
        print('Práctica 1 - Lenguajes Formales de Programación')
        print('*'*50,'\n')
        print('# SISTEMA DE INVENTARIO\n')
        print('''1. Cargar Inventario Inicial
2. Cargar instrucción de Movimiento
3. Crear Infome de Inventario
4. Salir\n''')
        
        op = input('Ingrese una opción: ')

        if op == '1':
            print('su opcion fue: 1. Cargar Inventario Inicial')
            leerArchivoEntrada()
        elif op == '2':
            print('su opcion fue: 2. Cargar instrucción de Movimiento')
        elif op == '3':
            print('su opcion fue: 3. Crear Infome de Inventario')
        elif op == '4':
            menu = False
            print('cerrando el programa...\n')
        else:
            print('Ingrese una opción valida')
            #menu() -> con recursividad 

    print('ya cerro el programa')

menu()
