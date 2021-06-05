import math
import numpy
import methods

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

for i in range(len(naves)):
    for j in range(size_ships[i]):
        xy = input("Ingresa la posiciòn en XY  para tu " +  naves[i] + "\n")
        y_num = methods.posY(xy[0])
        x = int(xy[1])
        tablero[y_num][x] = methods.ship_symbol(naves[i])


methods.printTablero(tablero)
