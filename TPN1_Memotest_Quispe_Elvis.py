from random import randint, shuffle, uniform, sample

def tablero(tamanio : int) ->list:
    '''
    PRE: Toma el valor entero que es el tamaño de la matriz
    POST: Retorna una lista de listas del tamaño dado
    '''
    matriz = []
    for filas in range(tamanio):
        asteriscos = []
        for columnas in range(tamanio):
            asteriscos.append("|**|")
        matriz.append(asteriscos)
    return matriz


def cartas(tam_matriz:int) -> list:
    '''
    PRE: Toma el tamaño de la matriz generada.
    POST: Retorna pares de cartas de numeros aleatorios.
    '''
    num_cartas = (tam_matriz * tam_matriz) // 2
    cartas = [0] * num_cartas
    cartas = sample(range(1, 201), num_cartas)
    cartas.extend(cartas)
    return cartas


def tablero_cartas(tamanio:int) -> list:
    '''
    PRE: Recibe el tamaño de la matriz
    POST: Retorna un tablero con las cartas de numeros aleatorios
    '''
    matrizz = tablero(tamanio)
    tam_matriz = len(matrizz)
    cartas_numeros = cartas(tam_matriz)
    tam_cartas_numeros = len(cartas_numeros)
    for filas in range(tam_matriz):
        matrizz[filas]
        for columnas in range(tam_matriz):
            matrizz[filas][columnas] = cartas_numeros.pop()
    mezclar_matriz_shuffle(matrizz)

    return matrizz


def printear_tablero(matriz: list) -> None:
    '''
     PRE: Recibe una matriz .
     POST: Imprime la matriz asignada.
    '''
    tamanio_matriz = len(matriz)
    for fila in range(tamanio_matriz):
        for columna in range(tamanio_matriz):
            print(matriz[fila][columna], end=" ")
        print("\n")


def mezclar_matriz_shuffle(matriz:list) -> None:
    '''
    PRE: Recibe la matriz a mezclar
    POST: -
    '''

    for filas in matriz:
        shuffle(filas)
    shuffle(matriz)

def carta_layout(tablero:list)->list:
    """
    PRE: Mezcla los tableros de forma que da vuelta las filas y la traspone.
    POST: Retorna el tablero mezclado.
    """

    for fila in tablero:
        fila.reverse()
    tablero = carta_fatality(tablero)

    return tablero

def carta_toti(tablerodadovuelta:list, tablanum:list) -> list:
    '''
    PRE: Recibe la matriz en juego y la matriz de cartas.
    POST: Modifica de forma azaroza a las matrices espejandolas de manera horizontal o vertical.
    '''
    sorteo = randint(1, 2)
    nuevo = []
    if sorteo == 1:                                           #Espejado Horizontal
        for fila in tablerodadovuelta:
            fila.reverse()
        nuevo.append(tablerodadovuelta)
        for fila in tablanum:
            fila.reverse()
        nuevo.append(tablanum)
        return nuevo

    else:                                                      #Espejado_Vertical
        nuevo.append(carta_toti_vertical(tablerodadovuelta))
        nuevo.append(carta_toti_vertical(tablanum))
        return nuevo


def carta_fatality(tablero:list) -> list:
    '''
    PRE: Recibe la matriz a modificar.
    POST: Retorna a la matriz de forma transpuesta.
    '''
    tam_tablero = len(tablero)
    transpuesta = []
    for filat in range(tam_tablero):
        transpuesta.append([])
        for columnat in range(tam_tablero):
            transpuesta[filat].append(tablero[columnat][filat])
    return transpuesta


def carta_toti_vertical(tablero:list) -> list:
    '''
     PRE: Recibe un tablero.
     POST: Retorna el tablero con los valores espejados verticalemente.
    '''
    new_table = carta_fatality(tablero)

    for fila in new_table:
        fila.reverse()
    new_table = carta_fatality(new_table)
    return new_table


def comodines_guardados(respuesta:str, comodines:dict) -> str:                       ##############################
    '''
    PRE: Recibe la respuesta en str y el diccionario de los comodines guardados.
    POST: Retorna un numero entero de forma de codigo para la carta seleccionada
    '''
    if respuesta == "s":
        if len(comodines) == 0:
            print("Todavia no tienes cartas ")

        else:
            print("Tus cartas son estas:")
            cartass = comodines.keys()
            print("\n".join(cartass))
            eleccion = input("Escribe cual carta quieres usar: ")
            eleccion.lower()
            if eleccion == 'replay':
                comodines['replay'] -= 1
                if comodines['replay'] == 0:
                    del comodines['replay']
                print("Hecho! Mareaste al rival\n")
                return 'replay'
            elif eleccion == 'layout':
                comodines['layout'] -= 1
                if comodines['layout'] == 0:
                    del comodines['layout']
                print("Hecho! Mareaste al rival\n")
                return 'layout'
            elif eleccion == 'toti':
                comodines['toti'] -= 1
                if comodines['toti'] == 0:
                    del comodines['toti']
                print("Hecho! Mareaste al rival\n")
                return 'toti'
            elif eleccion == 'fatality':
                comodines['fatality'] -= 1
                if comodines['fatality'] == 0:
                    del comodines['fatality']
                print("Hecho! Mareaste al rival\n")
                return 'fatality'
    else:
        return 'nada'



def efecto_comodin_tabla(clave: str, tablaasterisco: list, tabla_cartas: list) -> list:
    '''
    PRE: Recibe la clave de la carta de dato entero, recibe la matriz en juego y la matriz de cartas.
    POST: Retorna a la matriz modificada segun  la clave asignada.
    '''
    if clave== 'layout':
        tabla_layout=[]
        tablaasterisco = carta_layout(tablaasterisco)
        tabla_layout.append(tablaasterisco)
        tabla_cartas = carta_layout(tabla_cartas)
        tabla_layout.append(tabla_cartas)
        return  tabla_layout

    elif clave == 'toti':
        tabla_toti = []
        tablaasterisco = carta_fatality(tablaasterisco)
        tabla_toti.append(tablaasterisco)
        tabla_cartas = carta_fatality(tabla_cartas)
        tabla_toti.append(tabla_cartas)
        return tabla_toti
    else:
        espejado = carta_toti(tablaasterisco, tabla_cartas)
        return espejado


def menu_duracion_partida() -> int:
    '''
    PRE:-
    POST:Retorna el valor entero del tamaño de la matriz.
    '''
    print("Elija una opcion: ")
    opcion = int(input(" 1) Corto: tablero 4x4\n 2) Medio: tablero 8x8\n 3) Largo: tablero 12x12\n"))
    if opcion == 1:
        print("\nOpcion Guardada!")
        return 4
    elif opcion == 2:
        print("\nOpcion Guardada!")
        return 8
    elif opcion == 3:
        print("\nOpcion Guardada!")
        return 12

def pedir_prob_comodin(nombre_de_carta:str)->int:
    probabilidad=int(input(f"Ingrese una probabilidad del 1 al 100 para la carta {nombre_de_carta}"))
    while probabilidad not in range (1,101):
        probabilidad=print("vuelva a ingresar el valor: ")
    return probabilidad



def configuracion_juego() -> list:
    '''
    PRE: -
    POST: Retorna una lista con las configuraciones modificadas.
    '''
    print("Configuracion: \n")
    print("1) Duracion de la partida")
    print("2) Probabilidades de cartas")
    print("3) Atras")
    opcion = int(input(""))
    cambio_dur = 4
    cambio_prob = []
    cambio_total = []

    if opcion == 1:
        cambio_dur = menu_duracion_partida()
        cambio_total.append(cambio_dur)

    elif opcion == 2:
        cambio_prob.append(pedir_prob_comodin("replay"))
        cambio_prob.append(pedir_prob_comodin("layout"))
        cambio_prob.append(pedir_prob_comodin("toti"))
        cambio_prob.append(pedir_prob_comodin("fatality"))
        print("Opcion guardada!\n")
        return cambio_prob
    else:
        main()
    return cambio_total


def score(usuarios: dict, nombre_ganador: str) -> int:
    '''
    PRE: Recibe el diccionario de los jugadores y el nombre del ganador
    POST: retorna los puntos que adquirió dicho ganador
    '''
    if nombre_ganador not in usuarios:
        usuarios[nombre_ganador] = 0
        usuarios[nombre_ganador] += 1
    else:
        usuarios[nombre_ganador] += 1
    return usuarios[nombre_ganador]


def mostrar_score(lista_de_ganadores: dict) -> None:
    '''
    PRE: Toma el dicccionario donde tienen el nombre de los jugadores y sus respectivos puntos y los imprime.
    '''
    volver=1
    while volver!=0:
        itmganadores= lista_de_ganadores.items()
        puntos_ordenados={}

        for nombre, puntos in sorted(itmganadores, key = lambda puntos: puntos[1],reverse=True):
            puntos_ordenados[nombre]=puntos
        print("Tabla de ganadores: \n")
        for nombre in puntos_ordenados:
            print(nombre, ":", puntos_ordenados[nombre],"pts.")
        volver = int(input("\nPresione cero para volver al menu principal: "))


def usuarios() -> list:
    '''
    PRE:-
    POST: Retorna una lista con los nombres de los jugadores:
    '''
    nombre1 = input("Ingrese el nombre del jugador 1: ")
    nombre2 = input("Ingrese el nombre del jugador 2: ")
    Usuarios = [nombre1, nombre2]
    return Usuarios

def dado_probabilidad(carta:int, probabilidades:list) -> str:                                             #######################################
    '''
    PRE: Recibe el numero de comodin y una lista con la probabilidades de cada comodin
    POST: Retorna un codigo que representa el numero del comodin ganado.
    '''
    division = [i / 10 for i in probabilidades]
    if carta == 1:
        sorteo = uniform(1, 10)
        prob_carta_1 = division[0]
        if sorteo <= prob_carta_1:
            return "replay"
    elif carta == 2:
        sorteo = uniform(1, 10)
        prob_carta_2 = division[1]
        if sorteo <= prob_carta_2:
            codigo = 2
        return "layout"
    elif carta == 3:
        sorteo = uniform(1, 10)
        prob_carta_3 = division[2]
        if sorteo <= prob_carta_3:
            codigo = 3
        return "toti"
    elif carta == 4:
        sorteo = uniform(1, 10)
        prob_carta_4 = division[3]
        if sorteo <= prob_carta_4:
            codigo = 4
        return "fatality"



def validar_carta(codee:int) -> list:                                                                  #################################
    '''
    PRE: Recibe el numero entero del comodin.
    POST: Retorna una lista con la Respuesta, el numero y nombre de comodin.
    '''
    validacion_carta = []
    respuesta = ""
    if codee == 1:
        print("Has ganado la carta Replay")
        respuesta = input("Quieres usarla ahora? s/n:  ")
        validacion_carta.append(respuesta)
        validacion_carta.append(codee)
        validacion_carta.append('replay')

        return validacion_carta

    elif codee == 2:
        print("Has ganado la Carta Layout")
        respuesta = input("Quieres usarla ahora? s/n: ")
        validacion_carta.append(respuesta)
        validacion_carta.append(codee)
        validacion_carta.append('layout')

        return validacion_carta
    elif codee == 3:
        print("Has ganado la Carta Toti")
        respuesta = input("Quieres usarla ahora? s/n: ")
        validacion_carta.append(respuesta)
        validacion_carta.append(codee)
        validacion_carta.append('toti')

        return validacion_carta
    elif codee == 4:
        print("Has ganado la carta Fatality")
        respuesta = input("Quieres usarla ahora? s/n: ")
        validacion_carta.append(respuesta)
        validacion_carta.append(codee)
        validacion_carta.append('fatality')

        return validacion_carta


def validar_coordenadas(coordenadas:list, matriz:list) -> bool:
    '''
    PRE: Recibe la lista de coordenadas y la matriz de cartas.
    POST: Retorna un booleano.
    '''
    x = coordenadas[0]
    y = coordenadas[1]
    x2 = coordenadas[2]
    y2 = coordenadas[3]
    if matriz[x - 1][y - 1] == matriz[x2 - 1][y2 - 1]:
        print("Acertaste!!\n")
        return True

    else:
        print("No acertaste! \n")
        return False


def devolver_cartas(coordenadas: list, matriz: list) -> list:
    '''
    PRE: Recibe la lista de coordenadas y la matriz en juego.
    POST:Retorna a la matriz con las cartas tapadas en las coordenadas asignadas.
    '''
    matriz[coordenadas[0] - 1][coordenadas[1] - 1] = "|**|"
    matriz[coordenadas[2] - 1][coordenadas[3] - 1] = "|**|"
    return matriz


def dejar_dada_vuelta(coordenadas: list, matriz: list, tablaasterisco: list) -> list:
    '''
    PRE: Recibe la lista de coordenadas, la matriz de cartas y la matriz en juego.
    POST: Retorna la matriz con las cartas dada vuelta en las coordenadas asignadas
    '''
    tablaasterisco[coordenadas[0] - 1][coordenadas[1] - 1] = matriz[coordenadas[0] - 1][coordenadas[1] - 1]
    tablaasterisco[coordenadas[2] - 1][coordenadas[3] - 1] = matriz[coordenadas[2] - 1][coordenadas[3] - 1]
    return tablaasterisco


def pedir_coordenadas(tableroasteriscos: list, tam:int) -> list:
    '''
    PRE: Recibe el tablero en juego y el tamaño.
    POST: Retorna las coordenadas pedidas, evaluando si es que las coordenadas ya estan se elijieron o no.
    '''
    coordenadas = []
    coordenadasfila = int(input(f"Ingrese la coordenada fila del 1 al {tam}: "))
    coordenadas.append(coordenadasfila)
    coordenadascolumnas = int(input(f"Ingrese la coordenada columna del 1 al {tam}: "))
    coordenadas.append(coordenadascolumnas)
    while tableroasteriscos[coordenadas[0] - 1][coordenadas[1] - 1] != "|**|":
        print("Coordenada ya elegida elija otra\n")
        coordenadasfila = int(input(f"Ingrese la coordenada fila del 1 al {tam}: "))
        coordenadas[0]=coordenadasfila
        coordenadascolumnas = int(input(f"Ingrese la coordenada columna del 1 al {tam}: "))
        coordenadas[1]=coordenadascolumnas

    return coordenadas


def mostrar_coordenadas(coordenadass:list, matriz:list, tablerroasterisco:list, contador:int) -> None:
    '''
    PRE: Recibe la lista de coordenadas, la matriz de cartas, la matriz en juego y un contador
         para verificar si imprimir la primera coordenada o todas las coordenadas ingresadas.
    POST:-
    '''
    if contador == 0:
        x = coordenadass[0]
        y = coordenadass[1]
        tablerroasterisco[x - 1][y - 1] = matriz[x - 1][y - 1]
        printear_tablero(tablerroasterisco)


    else:
        x = coordenadass[0]
        y = coordenadass[1]
        x2 = coordenadass[2]
        y2 = coordenadass[3]
        tablerroasterisco[x - 1][y - 1] = matriz[x - 1][y - 1]
        tablerroasterisco[x2 - 1][y2 - 1] = matriz[x2 - 1][y2 - 1]
        printear_tablero(tablerroasterisco)
        contador = 0

def jugar_turno(nombre:str, comodines:dict, pares_ganados:int, tableroasteriscos:list, tabladecartas:list, tabla_rival_aster:list, tabla_rival_cartas:list, turnos:int, probabilidad:list, tamaño:int, turnorival:int)->list:
    turnos -= 1
    datos_cambiados = [tabla_rival_aster,tabla_rival_cartas,comodines,tableroasteriscos,pares_ganados,turnos,turnorival]
    print("--------------------------")
    print("Es el turno del jugador: ", nombre)
    numero = randint(1, 6)  # Es el numero del dado y la carta.
    n_comodin = dado_probabilidad(numero, probabilidad)  # Segun la probabilidad y el numero del dado, retornara o no el nombre del comodin.
    gano_replay = False
    if n_comodin == None:
        print("No has ganado niguna carta ")
    else:
        eleccion = input(f"Has ganado la carta {n_comodin}\nQuieres usar la carta ahora?: ")
        if eleccion == "s":
            if n_comodin == 'replay':  # Si responde "s" se aplica el comodin.
                gano_replay = True
                print("!Hecho, vas a tener un turno mas\n")
            else:  # Si no es replay entonces se aplica comodines que modifican la matriz del rival
                nuevas_tablas_rivalp2 = efecto_comodin_tabla(n_comodin, tabla_rival_aster, tabla_rival_cartas)
                tabla_rival_aster = nuevas_tablas_rivalp2[0]
                tabla_rival_cartas = nuevas_tablas_rivalp2[1]
                datos_cambiados[0] = tabla_rival_aster
                datos_cambiados[1] = tabla_rival_cartas

            print("Hecho mareaste a tu rival!\n")  # Modifica a la matriz de cartas y la que esta en juego del rival.
        else:
            if n_comodin not in comodines:  # En caso de que no este el nombre de la carta en el dict lo agrega y le suma 1.
                comodines[n_comodin] = 0
                comodines[n_comodin] += 1
            else:
                comodines[n_comodin] += 1  # En caso de que ya este le suma de a 1 valor.
            print("!Carta guardada\n")
    datos_cambiados[2] = comodines
    respuesta = input("Quieres usar alguna carta guardada? s/n: ")
    nombre_carta = comodines_guardados(respuesta, comodines)  # Si quieres usar una carta guardada el usuario va a poder decidir cual.
    if nombre_carta == 'replay':  # Dependiendo del nombre del comodin ejecutara o no el comodin.
        gano_replay = True
        print("!Hecho, vas a tener un turno mas\n")
    elif nombre_carta != 'nada':
        nuevas_tablas_rivalp2 = efecto_comodin_tabla(nombre_carta, tabla_rival_aster, tabla_rival_cartas)
        tabla_rival_aster= nuevas_tablas_rivalp2[0]
        tabla_rival_cartas = nuevas_tablas_rivalp2[1]
        datos_cambiados[0]=tabla_rival_aster
        datos_cambiados[1]=tabla_rival_cartas

    printear_tablero(tableroasteriscos)
    print("adivina las cartas de tu rival!\n")
    coord = pedir_coordenadas(tableroasteriscos, tamaño)  # Pide la coordenadas y las muestra.
    mostrar_coordenadas(coord, tabladecartas, tableroasteriscos, 0)
    coord2 = pedir_coordenadas(tableroasteriscos, tamaño)
    coord_general = coord + coord2
    mostrar_coordenadas(coord_general, tabladecartas, tableroasteriscos, 1)
    validacion = validar_coordenadas(coord_general, tabladecartas)  # Verifica si las coordenadas seleccionadas son iguales.

    if validacion:  # Si son iguales suma los pares obtenidos del jugador y el turno.
        pares_ganados += 1
        turnos+= 1
        tableroasteriscos = dejar_dada_vuelta(coord_general, tabladecartas, tableroasteriscos)  # Deja las cartas a la vista.
        datos_cambiados[3] = tableroasteriscos
        if gano_replay:  # Si gano el comodin replay suma otro turno mas.
            turnos += 1
    else:  # Si no son iguales da vuelta las cartas.
        tableroasteriscos = devolver_cartas(coord_general, tableroasteriscos)
        datos_cambiados[3] = tableroasteriscos
        if gano_replay:
            turnos += 1
        else:
            turnos -= 1
            turnorival = 1
    datos_cambiados[4]=pares_ganados
    datos_cambiados[5]=turnos
    datos_cambiados[6]=turnorival
    return datos_cambiados

def desarrollo_del_juego(tam:int, prob:list) -> str:
    '''
    PRE: Recibe el tamaño de la matriz para el juego y la lista de probabilidades de los comodines.
    POST: Retorna el nombre del ganador.
    '''
    nombres = usuarios() #Nombres de los jugadores.
    pares_p1 = 0
    pares_p2 = 0
    cartas_guardadas1 = {}
    cartas_guardadas2 = {}
    tablaasteriscos1 = tablero(tam)  #La tabla 1 dada vuelta y la que va estar en juego le pertenece a jugador 1 y la juega jugador 2.
    tablaasteriscos2 = tablero(tam)  #La tabla 2 dada vuelta y la que va estar en juego le pertenece a jugador 2 y la juega jugador 1.
    tabla1 = tablero_cartas(tam)     #La tabla 1 de cartas le pertenece a jugador 1 y la juega jugador 2.
    tabla2 = tablero_cartas(tam)     #La tabla 2 de cartas le pertenece a jugador 2 y la juega jugador 1.
    turno1 = 1
    turno2 = 0
    game = True
    #print(tabla1)
    #print(tabla2)
    while game:
        while turno1 > 0:
            datos_cambiados = []
            datos_cambiados = jugar_turno(nombres[0],cartas_guardadas1,pares_p1,tablaasteriscos2,tabla2,tablaasteriscos1,tabla1,turno1,prob,tam,turno2)
            tablaasteriscos1 = datos_cambiados[0]
            tabla1 = datos_cambiados[1]
            cartas_guardadas1 = datos_cambiados[2]
            tablaasteriscos2 = datos_cambiados[3]
            pares_p1 = datos_cambiados[4]
            turno1 = datos_cambiados[5]
            turno2 = datos_cambiados[6]
            if pares_p1 == ((tam * tam) // 2):
                turno1 = 0
                game = False
            elif pares_p2 == ((tam * tam) // 2):
                turno2=0
                game = False

        while turno2 > 0:
            datos_cambiados = []
            datos_cambiados = jugar_turno(nombres[1],cartas_guardadas2,pares_p2,tablaasteriscos1,tabla1,tablaasteriscos2,tabla2,turno2,prob,tam,turno1)
            tablaasteriscos2 = datos_cambiados[0]
            tabla2 = datos_cambiados[1]
            cartas_guardadas2 = datos_cambiados[2]
            tablaasteriscos1 = datos_cambiados[3]
            pares_p2 = datos_cambiados[4]
            turno2 = datos_cambiados[5]
            turno1 = datos_cambiados[6]
            if pares_p1 == ((tam * tam) // 2):
                turno1 = 0
                game = False
            elif pares_p2 == ((tam * tam) // 2):
                turno2 = 0
                game = False

    #Si termina el juego verificara quien es el jugador que gano primero y retornara el nombre de este.
    else:
        if pares_p1 == ((tam * tam) // 2):
            print(f"Ha ganado el jugador {nombres[0]} ")
            return nombres[0]

        else:
            print(f"Ha ganado el jugador {nombres[1]}")
            return nombres[1]


def menu_opciones() -> int:
    '''
    PRE:-
    POST: Retorna el numero de opcion elegida por el usuario.
    '''
    print("******Bienvenidos al juego MEMOTEST******")
    print("Marque 1) para jugar")
    print("Marque 2) para la configuración del juego")
    print("Marque 3) para ver el score")
    print("Marque 4) para salir del juego")
    opcion = int(input(""))
    return opcion


def main() -> None:
    ejecucion = True
    tabla = 4  #El tamaño de la matriz por defecto.
    probabilidad = [50, 50, 50, 50] #Las probabilidades de la carta por defecto.
    ganadores = {}
    while ejecucion:
        opcion = menu_opciones()
        duracion = tabla
        prob = probabilidad
        datos_cambiados = []
        if opcion == 1:                                         #Si opcion es 1 inicia el juego.
            ganador = desarrollo_del_juego(duracion, prob)
            ganadores[ganador] = score(ganadores, ganador)

        elif opcion == 2:  # Si opcion es 2 entonces ingresa a la configuracion del juego.
            datos_cambiados = configuracion_juego() #La lista de los datos cambiados.
            if len(datos_cambiados) == 1: #Si la lista solo tiene un valor entonces se trata del tamaño de la matriz.
                tabla = datos_cambiados[0]
            elif len(datos_cambiados) != 1: #Si la lista tiene varios valores, se establecieron las probabilidades.
                probabilidad = datos_cambiados

        elif opcion == 3:
            mostrar_score(ganadores)

        else:
            ejecucion = False

    print("Fin del Programa")

main()