import random

def posY(letra):

    """
    Retorna un nùmero que representa una posiciòn en un 
    tablero
    letra: posciòn en el tablero de forma alfabetica
    """
    if(letra == 'A'):
        return 0
    elif(letra == 'B'):
        return 1
    elif(letra == 'C'):
        return 2
    elif(letra == 'D'):
        return 3
    elif(letra == 'E'):
        return 4
    elif(letra == 'F'):
        return 5
    elif(letra == 'G'):
        return 6
    elif(letra == 'H'):
        return 7
    elif(letra == 'I'):
        return 8
    elif(letra == 'J'):
        return 9
    else:
        pass


def ship_symbol(ship):

    """
    Retorna un caràcter segùn el nombre  de barco
    ship: nombre del barco 
    """
    if(ship == "Portaviones"):
        return 'P'
    elif(ship == "Battleship"):
        return 'B'
    elif(ship == "Crucero de batalla"):
        return 'C'
    elif(ship == "Submarino"):
        return 'S'
    elif(ship == "Lancha"):
        return 'L'
    else:
        pass


def posAlp(posy):
    """
    Retorna la letra que representa la posiciòn en el eje Y
    posy: valor int que representa una posiciòn Y en un tablero
    """

    if(posy == 0):
        return 'A'
    elif(posy == 1):
        return 'B'
    elif(posy == 2):
        return 'C'
    elif(posy == 3):
        return 'D'
    elif(posy == 4):
        return 'E'
    elif(posy == 5):
        return 'F'
    elif(posy == 6):
        return 'G'
    elif(posy == 7):
        return 'H'
    elif(posy == 8):
        return 'I'
    elif(posy == 9):
        return 'J'
    else:
        pass


def printTablero(tablero):

    """
    Da formato de tablero a un array 2D y lo imprime en pantalla
    tablero: array 2D de tipo char
    """
    print("    0   1   2   3   4   5   6   7   8   9")
    row = ""
    for i in range(10):
        for j in range(10):
            row = row + " | "+ tablero[i][j] 

        print(posAlp(i) + row)
        row = ""


def fillTableroPc(tablero, listaXY):
    """
    Devuelve una matriz con las posiciones de los barcos segun
    la lista de posiciones
    tablero: matrix vacia de 10x10
    listaXY: posiciones deseadas para la matrix en formato alfanumerico
    """
    tableroPc = tablero
    for i in range(0, 5):
        pos = listaXY[i]
        y_num = posY(pos[0])
        x = int(pos[1])
        tableroPc[y_num][x] = ship_symbol("Portaviones")

    for i in range(5, 9):
        pos = listaXY[i]
        y_num = posY(pos[0])
        x = int(pos[1])
        tableroPc[y_num][x] = ship_symbol("Battleship")

    for i in range(9, 12):
        pos = listaXY[i]
        y_num = posY(pos[0])
        x = int(pos[1])
        tableroPc[y_num][x] = ship_symbol("Crucero de batalla")

    for i in range(12, 14):
        pos = listaXY[i]
        y_num = posY(pos[0])
        x = int(pos[1])
        tableroPc[y_num][x] = ship_symbol("Submarino")

        pos = listaXY[14]
        y_num = posY(pos[0])
        x = int(pos[1])
        tableroPc[y_num][x] = ship_symbol("Lancha")

    return tableroPc

def PC_Ataca(listaAtaques):
    """
    genera una coordenada alfanumerica con el fin de atacar un tablero
    listaAtaques: guarda los anteriores posiciones atacadas 
    """
    y_Axis = ['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J']
    x = random.randint(0,9)
    y = random.choice(y_Axis)
    pos = y + str(x)
    while(pos in listaAtaques):
        x = random.randint(0,9)
        y = random.choice(y_Axis)
        pos = y + str(x)

    return pos


def Coordenadas_Disparo(pos):
         
    """
    verifica si pos corresponde a una coordenada dentro del rango 
    alfanumerico de [A,J] y [0. 9]
    retorno: True si se haya en los rangos
    de lo contrario False
    """
    x_Axis = ['0','1','2','3','4','5','6','7','8','9']     
    y_Axis = ['A','B','C','D','E', 'F', 'G', 'H', 'I', 'J']
    if(pos[0] in y_Axis and pos[1] in x_Axis):
        return True

    else:
        return False
    

def Verificar_acierto(tablero_PC, ataque, tablero_Marcador):

    """
    verifica si la pos de ataque en tablero_PC se encentra vacia o
    contiene un barco
    retorna una matriz con los respectivos aciertos (A) y fallos (X)
    """
    y = posY(ataque[0])
    x = int(ataque[1])

    if(tablero_PC[y][x] != " "):
        tablero_Marcador[y][x] = "A"

    else:
        tablero_Marcador[y][x] = "X"

    return tablero_Marcador


def Verificar_fallo(tablero, ataque):
    y = posY(ataque[0])
    x = int(ataque[1])

    if(tablero[y][x] != " "):
        return True

    else:
        return False


def Barco_atacado(tablero, ataque):
    """
    Regresa el simbolo del barco segun
    las coordenadas de ataque
    """

    y = posY(ataque[0])
    x = int(ataque[1])

    return tablero[y][x]

