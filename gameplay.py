import methods
import random
import copy

xy = ""
listaXY = []
lista_ataques_pc = []

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
tableroPC = copy.deepcopy(tablero)
tablero_Marcador = copy.deepcopy(tablero)


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

select = random.randint(1,3)
selected = str(select)
file_tablero = "conf"+selected+".txt"
f = open(file_tablero, 'r')
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
#methods.printTablero(tableroPC)
#ataque = methods.PC_Ataca(lista_ataques_pc)
#print(ataque)

tablero = copy.deepcopy(tableroPC)

jugar = True

while(jugar):

    #Se solicita al usuario una coordenada para atacar
    #y se comprueba que este dentro del tablero
    pos = input("Coordenada de ataque: ")
    check_ataque = methods.Coordenadas_Disparo(pos)
    while(check_ataque == False):
        print("¡¡Coordenada invalida!! \n")
        pos = input("Ingrese coordenada de ataque ")
        check_ataque = methods.Coordenadas_Disparo(pos)


    acierto_user = methods.Verificar_fallo(tableroPC, pos)
    if(acierto_user):
        print("Acertó")
    else:
        print("Falló")

    tablero_Marcador = methods.Verificar_acierto(tableroPC, pos, tablero_Marcador)
    
    
    methods.printTablero(tablero_Marcador)     
    ataque = methods.PC_Ataca(lista_ataques_pc)
    print("PC ataca "+ ataque)
    acierto = methods.Verificar_fallo(tablero, ataque)
    if(acierto):
        print("Acertó")
    else:
        print("Falló")

    lista_ataques_pc.append(ataque)
    tablero = methods.Verificar_acierto(tablero, ataque, tablero)
    methods.printTablero(tablero)
    
    print("\n"*3)
    

