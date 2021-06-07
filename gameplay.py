import methods

xy = ""
listaXY = []

naves = ["Portaviones", "Battleship", "Crucero de batalla", "Submarino", "Lancha"]
size_ships = [5,4,3,2,1]

row0 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row1 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row2 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row3 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row4 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row5 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row6 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row7 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row8 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
row9 = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

tablero = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9]
tableroPC = tablero

#Se le solicita al usuario las posiciones para el tablero
#Y se almacenan en la matriz

"""
for i in range(len(naves)):
    for j in range(size_ships[i]):
        xy = input("Ingresa la posiciòn en XY  para tu " +  naves[i] + "\n")
        y_num = methods.posY(xy[0])
        x = int(xy[1])
        tablero[y_num][x] = methods.ship_symbol(naves[i])

"""

#se crea una lista con las posiciones alfanumericas resultantes de la 
#lectura de un archivo de configuracion seleccionado aleatoriamente

f = open('conf1.txt', 'r')
for line in f:
    for i in range(13, len(line)):
        if(line[i] == ',' or line[i] == "\n"):
            listaXY.append(xy)
            xy = ""
        elif(line[i] != ","):
            xy = xy + line[i]

        else:
            pass

tableroPC = methods.fillTableroPc(tableroPC, listaXY)
methods.printTablero(tableroPC)
