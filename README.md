# TP1-ALGO1

                                       Algoritmos y Programación I 
                                       Trabajo Práctico N°1 
                                       1er Cuatrimestre 2021
Este juego se basa en el histórico Memotest que jugábamos cuando éramos chicos (al menos Bruno 
y yo). Cada jugador tiene un tablero que tiene N fichas distribuidas en M filas y M columnas de las 
cuales se desconoce su contenido hasta darlas vuelta, pero siempre se sabe que hay 2 fichas de cada 
tipo. Los jugadores deberán encontrar los pares de fichas idénticos en el tablero del oponente. En 
caso de no encontrarlos las fichas volverán a su posición oculta original. En caso de acertar y 
encontrar el jugador puede volver a jugar en el mismo turno, intentando ubicar otro par. 
La partida termina una vez que todos los pares de un tablero son descubiertos y el ganador será el 
jugador que lo haga primero. 


Pequeñas modificaciones al juego original 
Al llegar un turno al jugador, se tira un dado de varias caras donde el resultado puede ser que 
obtenga o no una carta comodín en base a probabilidades que se definen en el menú. Por turno solo 
sale como máximo 1 carta comodín. Las cartas comodín existentes son: 
1) Carta Replay: Permite hacer un intento más durante el turno. 
2) Carta Layout: Redistribuye todas las fichas del tablero del jugador que la tiene de manera 
aleatoria 
3) Carta Toti: Espeja el tablero del jugador que la tiene de forma azarosa, puede ser horizontal 
o vertical. 
4) Carta Fatality: Traspone el tablero del jugador que la tiene 
El jugador puede decidir jugar su carta comodín en dicho turno o guardarla para otro turno. Se 
pueden acumular más de una carta comodín de cada tipo 
Los niveles de duración son corto, medio y largo. La duración estará representada con la cantidad de 
filas y columnas presentes en el tablero. Por defecto será el tamaño Corto. 
Corto: tamaño menor a 4x4 
Medio: tamaño menor a 8x8 
Largo: tamaño mayor a 12x12 


El programa deberá contener un un menú que permita: 
a- Comenzar una nueva partida solicitando el nombre de cada jugador 
b- Definir los parámetros de juego (duración, probabilidad de Replay, probabilidad 
de Layout, probabilidad de Toti y probabilidad de Fatality) 
c- Mostar el score de las últimas 4 partidas ordenadas por quien ganó más partidas, 
indicando nombre y cantidad de partidas 
SOLO SE PERMITEN UTILIZAR LOS CONOCIMIENTOS ADQUIRIDOS HASTA EL MOMENTO Y SE 
PROHIBE EL USO DE BIBLIOTECAS DE FUNCIONES EXTERNAS, EXCEPTUANDO RANDOM.
