import random
#Solamente son funciones las opciones de, jugar, cambiar parámetros, y ver ayuda.
#Las demás solo muestran texto que no depende de más interacción del usuario, por lo que no se considera necesario añadirlas como funciones.

import time

def jugar(fallos):
#La función para jugar devuelve una lista con la cantidad de victorias y derrotas en las posiciones 0 y 1 respectivamente.
#Toma como valor de entrada la cantidad de intentos, ya sea por defecto o cambiada por el usuario.

    palabra = lista_activa[random.randint(0, len(lista_activa)-1)]
    salida = False
    win_lose = [0, 0]
    respuesta = [i for i in palabra]
    letras = ["_"]*len(palabra)
    print(letras)

    primera_vez = True

    while not salida:

        if fallos <=0:

            if primera_vez:
                print("Perdió...")
            primera_vez = False

            win_lose[0] += 0
            win_lose[1] += 1

            try:
                salir = int(input('¿Desea salir?\n1. Salir\n2. Jugar de nuevo\nOpción: '))
                if salir == 1:
                    salida = True
                elif salir == 2:
                    jugar(intentos)
                else:
                    print('Valor incorrecto, intente de nuevo')

                    time.sleep(1.5)

            except ValueError: 
                print('Valor incorrecto, intente de nuevo')
                
                time.sleep(1.5)
            

        elif letras == respuesta:
            print("¡Ganó!")
            win_lose[0] += 1
            win_lose[1] += 0
            salir = int(input('¿Desea salir?\n1. Salir\n2. Jugar de nuevo\nOpción: '))
            if salir == 1:
                salida = True
            elif salir == 2:
                jugar(intentos)
            else:
                salir = int(input('Valor incorrecto, intente de nuevo: '))

        else:
            malas = 0
            letter = (input('Digite la letra: '))

            for i in range(len(palabra)):
                if letter.upper() == palabra[i].upper():
                    letras[i] = palabra[i]

                else:
                    malas += 1

            if malas >= len(palabra):
                fallos -=1
                print(letras)
                print("Fallos restantes:", fallos)

            else:
                print(letras)
                print("Fallos restantes:", fallos)
    return win_lose

    

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


def ayuda(opcion):
#La función de ayuda simplemente imprime la ayuda para la sección del programa escogida por el ususario anteriormente.
#De esta forma no toma tanto espacio en el menú principal
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

file_flwr = open("floresyplantas.txt", "r")
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

victorias = 0
derrotas = 0
vic_der = [0, 0]

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
        vic_der = jugar(intentos)
        victorias += vic_der[0]
        derrotas += vic_der[1]

    elif opcion_menu == 2:
        print('Cambio de parámetros')
        print('Digite el número correspondiente a lista que quiere usar.')
        print('Listas:')
        print('1. Plantas')
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
        print('Resultados de la sesión actual')
        print('Partidas ganadas:', victorias)
        print('Partidas perdidas:', derrotas)

    elif opcion_menu == 4:
        print("Digite la opcion sobre la que quiere ayuda:")
        print('1. Jugar')
        print('2. Cambiar parámetros')
        print('3. Mostrar resultados')
        print('4. Salir')
        opcion_ayuda = int(input(''))
        ayuda(opcion_ayuda)

    elif opcion_menu == 5:
        print('Programa hecho por Andrés Cedeño, [espacio para nombre de alex], y [espacio para el nombre de sergio]\ncomo proyecto del curso de Introducción a la Computación impartido por\nIgnacio Díaz en el primer semestre, 2024')

    elif opcion_menu == 6:
        print('Gracias por jugar')
        bandera_salida = True

    else:
        print('Opción invalida')

#Nota, el programa no lee caractéres especiales como tildes o la Ñ desde los archivos por un problema de codificaciión de datos