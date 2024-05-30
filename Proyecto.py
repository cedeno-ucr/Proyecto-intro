#Aquí inicia la vara esta
def jugar():
    print('Trabajo en proceso')

def parametros():
    print('Trabajo en proceso')

def resultados():
    print('Trabajo en proceso')

def ayuda(opcion):
    if opcion == 1:
        print(f'Para jugar, una palabra aleatoria será elegida de entre la')
        print(f'o las listas escogidas en Parámetros. Usted deberá digitar')
        print(f'letra a letra las letras en la palabra en la cantidad de')
        print(f'intentos establecida en Parámetros. De encontar todas las')
        print(f'letras, ganará. Si no lo logra en la cantidad de intentos o')
        print(f'menos, perderá.')
        return
    elif opcion == 2:
        print('Trabajo en progreso')
        return
    elif opcion == 3:
        print(f'En este menú se muestran la cantidad de partidas ganadas y')
        print(f'perdidas en la sesión actual.')
        return
    elif opcion == 4:
        print('Volviendo al menú principal.')
        return
    else:
        print(f'Error. Opción incorrecta')
        return



def acerca_de():
    print('Programa hecho por Andrés Cedeño, Alex Ulate, y Sergio [apellido de sergio]\ncomo proyecto del curso de Introducción a la Computación impartido por\nIgnacio Díaz en el primer semestre, 2024')
    return



bandera_salida = False

while not bandera_salida:
    print('----Ahorcado----')
    print('1. Jugar')
    print('2. Parámetros')
    print('3. Mostrar resultados')
    print('4. Ayuda')
    print('5. Acerca de...')
    print('6. Salir')

    opcion_menu = int(input('Digite su opción: '))
    
    if opcion_menu == 1:
        jugar()
    elif opcion_menu == 2:
        parametros()

    elif opcion_menu == 3:
        resultados()

    elif opcion_menu == 4:
        print("Digite la opcion sobre la que quiere ayuda:")
        print('1. Jugar')
        print('2. Cambiar parámetros')
        print('3. Mostrar resultados')
        print('4. Salir')
        opcion_ayuda = int(input(''))
        ayuda(opcion_ayuda)

    elif opcion_menu == 5:
        acerca_de()

    elif opcion_menu == 6:
        print('Gracias por jugar')
        bandera_salida = True

    else:
        print('Opción invalida')