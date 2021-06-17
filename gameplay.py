import methods
import random
import copy
from time import sleep

xy = ""
listaXY = []
lista_ataques_pc = []
barcos_hundidos_PC = []
barcos_hundidos_user = []

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

def User_ataca():

    # Se solicita al usuario una coordenada para atacar
    # y se comprueba que este dentro del tablero
    pos = input("Coordenada de ataque: ")
    check_ataque = methods.Coordenadas_Disparo(pos)
    while(check_ataque == False):
        print("¡¡Coordenada invalida!! \n")
        pos = input("Ingrese coordenada de ataque ")
        check_ataque = methods.Coordenadas_Disparo(pos)


    acierto_user = methods.Verificar_fallo(tableroPC, pos)
    if(acierto_user):
        print("Acertó")
        barco = methods.Barco_atacado(tableroPC, pos)
        if(barco in barcos_hundidos_PC):
            pass
        else:
            barcos_hundidos_PC.append(barco)
    else:
        print("Falló")

    #tablero_Marcador = methods.Verificar_acierto(tableroPC, pos, tablero_Marcador)
    methods.printTablero(methods.Verificar_acierto(tableroPC, pos, tablero_Marcador))


def PC_ataca(tablero):

    ataque = methods.PC_Ataca(lista_ataques_pc)
    print("PC ataca "+ ataque)
    acierto = methods.Verificar_fallo(tablero, ataque)
    if(acierto):
        print("Acertó")
        barco = methods.Barco_atacado(tablero, ataque)
        if(barco in barcos_hundidos_user):
            pass
        else:
            barcos_hundidos_user.append(barco)
    else:
        print("Falló")

    lista_ataques_pc.append(ataque)
    tablero = methods.Verificar_acierto(tablero, ataque, tablero)
    methods.printTablero(tablero)

players = ['user', 'pc']
first = random.choice(players)

while(jugar):

    if(first == 'user'):
        continuar = True
        print("Inicia el usuario \n")
        while(continuar):
            User_ataca()
            PC_ataca(tablero)
            #permite visualizar la info al usuario
            sleep(1)
            print("\n"*7)

            if(len(barcos_hundidos_user) == 5 or len( barcos_hundidos_PC) == 5):
                if(first == 'user' and len(barcos_hundidos_PC) == 5):
                    PC_ataca(tablero)

                else:
                    User_ataca()

                if(len(barcos_hundidos_user) == 5 and len(barcos_hundidos_PC) == 5):
                    print("\n ***Empate*** \n")
                    continuar = False

                elif(len(barcos_hundidos_user) == 5 and len(barcos_hundidos_PC) != 5):
                    print("\n ***PC gana*** \n")
                    continuar = False

                elif(len(barcos_hundidos_user) != 5 and len(barcos_hundidos_PC) == 5):
                    print("\n ***Usuario gana*** \n")
                    continuar = False

    else:
        continuar = True
        print("Inicia PC")
        while(continuar):
            PC_ataca(tablero)
            User_ataca()
            # permitir visualizar la informaciona al usuario
            sleep(1)
            print("\n"*7)
            if(len(barcos_hundidos_user) == 5 or len( barcos_hundidos_PC) == 5):
                if(first == 'user' and len(barcos_hundidos_PC) == 5):
                    PC_ataca(tablero)

                else:
                    User_ataca()

                if(len(barcos_hundidos_user) == 5 and len(barcos_hundidos_PC) == 5):
                    print("\n***Empate***\n")
                    continuar = False

                elif(len(barcos_hundidos_user) == 5 and len(barcos_hundidos_PC) != 5):
                    print("\n ***PC gana***\n")
                    continuar = False

                elif(len(barcos_hundidos_user) != 5 and len(barcos_hundidos_PC) == 5):
                    print("\n ***Usuario gana*** \n")
                    continuar = False


    jugar = False
"""    
    cont = input("Desea continua Y/N ?")
    if(jugar == 'Y'):
        jugar = True
    else:
        jugar = False
"""
