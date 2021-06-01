import math
import numpy

naves = ["Portaviones", "Battleship", "Crucero de batalla", "Submarino", "Lancha"]
size = [5,4,3,2,1]

tablero = numpy.zeros((10,10))

tablero[5,3] = 8
print(tablero)



"""
for i in range(len(naves)):
    for j in range(size[i]):
        input("Ingresa las posiciones para tu " +  naves[i])
"""
