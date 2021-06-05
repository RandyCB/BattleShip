
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
    print("    0   1   2   3   4   5   6   7    8   9")
    row = ""
    for i in range(10):
        for j in range(10):
            row = row + " | "+ tablero[i][j] 

        print(posAlp(i) + row)
        row = ""
