#Aquí inicia la vara esta
def jugar():
    print('Trabajo en proceso')

def parametros():
    print('Trabajo en proceso')

def resultados():
    print('Trabajo en proceso')

def ayuda():
    print('Trabajo en proceso')

def acerca_de():
    print('Trabajo en proceso')



bandera_salida = False

while not bandera_salida:
    print('----Ahorcado----')
    print('1. Jugar')
    print('2. Cambiar parámetros')
    print('3. Mostrar resultados')
    print('4. Ayuda')
    print('5. Acerca de...')
    print('6. Salir')
    opcion_menu = int(input('Digite su opción:'))
    if opcion_menu == 1:
        jugar()
        
    if opcion_menu == 2:
        parametros()

    if opcion_menu == 3:
        resultados()

    if opcion_menu == 4:
        ayuda()

    if opcion_menu == 5:
        acerca_de()

    if opcion_menu == 6:
        print('Gracias por jugar')
        bandera_salida = True

    else:
        print('Opción invalida')