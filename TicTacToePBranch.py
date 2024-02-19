from PBranchFunctions import *

listaPosiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]

tablero(listaPosiciones)

respuestaVerificar = 0
respuestaGanador = 0
x = 1
while x <= 9:
    respuestaGanador = verificarGanador(listaPosiciones)
    if respuestaGanador == 0:
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 9:
            respuestaUsuario = int(input("Favor de ingresar la posición en la que desee ingresar una X: "))
            respuestaVerificar = verificarPosicion(respuestaUsuario, listaPosiciones)
            if respuestaVerificar == 0:
                continue
            elif respuestaVerificar == 1:
                listaPosiciones[respuestaUsuario - 1] = "X"
                tablero(listaPosiciones)
                x = x + 1
        elif x == 2 or x == 4 or x == 6 or x == 8:
            respuestaUsuario = int(input("Favor de ingresar la posición en la que desee ingresar una O: "))
            respuestaVerificar = verificarPosicion(respuestaUsuario, listaPosiciones)
            if respuestaVerificar == 0:
                continue
            elif respuestaVerificar == 1:
                listaPosiciones[respuestaUsuario - 1] = "O"
                tablero(listaPosiciones)
                x = x + 1
    elif respuestaGanador == 1:
        break