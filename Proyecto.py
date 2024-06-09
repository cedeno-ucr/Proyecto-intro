def jugar():
    print('Trabajo en proceso')

def parametros(lista, vidas):
    lista_temporal = []
    vidas_temporal = 0
    bandera_listas = False
    bandera_vidas = False

    while not bandera_listas:
        if lista == 0:
            lista_temporal = list_all
            bandera_listas = True
        elif lista == 1:
            lista_temporal = list_flwr
            bandera_listas = True
        elif lista == 2:
            lista_temporal = list_sprt
            bandera_listas = True
        elif lista == 3:
            lista_temporal = list_anim
            bandera_listas = True
        elif lista == 4:
            lista_temporal = list_ctry
            bandera_listas = True
        else:
            lista  = int(input('Entrada incorrecta para elección de lista, intente de nuevo: '))


    while not bandera_vidas:
        if vidas == 1:
            vidas_temporal = 15
            bandera_vidas = True
        elif vidas == 2:
            vidas_temporal = 10
            bandera_vidas = True
        elif vidas == 3:
            vidas_temporal = 5
            bandera_vidas = True
        else:
            vidas = int(input('Entrada incorrecta para elección de dificultad, intente de nuevo: '))

    return lista_temporal, vidas_temporal

def resultados():
    print('Trabajo en proceso')

def ayuda(opcion):
    if opcion == 1:
        print('Para jugar, una palabra aleatoria será elegida de entre la')
        print('o las listas escogidas en Parámetros. Usted deberá digitar')
        print('letra a letra las letras en la palabra fallando como mucho')
        print('la cantidad de "vidas" establecida en Parámetros. Cada vez')
        print('que falle, su cantidad de "vidas" se reducirá en 1. Si la')
        print('cantidad de vidas llega a 0, perderá. De encontar todas')
        print('las letras antes de eso, ganará.')

    elif opcion == 2:
        print('Aquí podrá cambiar ciertas opciones para jugar. Estas son')
        print('la dificultad, determinada por la cantidad de "vidas", y')
        print('la lista de palabras que quiera usar. La cantidad de "vidas"')
        print('para Fácil es 15, para Normal es 10, y para Difícil es 5')
        print('Por defecto, están disponibles todas las palabras y')
        print("la dificultad es Normal.")

    elif opcion == 3:
        print('En este menú se muestran la cantidad de partidas ganadas y')
        print('perdidas en la sesión actual.')

    elif opcion == 4:
        print('Volviendo al menú principal.')

    else:
        print('Error. Opción incorrecta')

def acerca_de():
    print('Programa hecho por Andrés Cedeño, Alex Ulate, y Sergio [apellido de sergio]\ncomo proyecto del curso de Introducción a la Computación impartido por\nIgnacio Díaz en el primer semestre, 2024')

file_flwr = open("flores.txt", "r")
list_flwr = file_flwr.readline().split()
file_flwr.close()

file_sprt = open("deportes.txt", "r")
list_sprt = file_sprt.readline().split()
file_sprt.close()

file_anim = open("animales.txt", "r")
list_anim = file_anim.readline().split()
file_anim.close()

file_ctry = open("paises.txt", "r")
list_ctry = file_ctry.readline().split()
file_ctry.close()

list_all = list_anim+list_ctry+list_flwr+list_sprt

lista_activa = list_all

intentos = 10


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
        print('Cambio de parámetros')
        print('Digite el número correspondiente a lista que quiere usar.')
        print('Listas:')
        print('1. Flores')
        print('2. Deportes')
        print('3. Animales')
        print('4. Países')
        print('0. Lista Combinada')
        numero_lista = int(input('Lista: '))

        print('Digite el número correspondiente a la dificultad que quiera usar.')
        print('1. Fácil')
        print('2. Normal')
        print('3. Difícil')
        numero_dificultad = int(input('Dificultad: '))

        lista_activa, intentos = parametros(numero_lista, numero_dificultad)

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

#Nota, el programa no lee caractéres especiales como tildes o la Ñ desde los archivos por un problema de codificaciión de datos