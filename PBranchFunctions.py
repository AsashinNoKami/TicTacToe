def tablero(lista):
    print("Tablero de juego:")
    print("")
    print(lista[0], "|", lista[1],"|", lista[2])
    print("--|---|--")
    print(lista[3], "|", lista[4],"|", lista[5])
    print("--|---|--")
    print(lista[6], "|", lista[7],"|", lista[8])
    print("")
    print("Instrucciones:")
    print("1. Insertar un numero entre 1 al 9 para elegir la posicion.")
    print("2. Se tienen que llenar las 9 posiciones para terminar el juego.")
    print("3. El jugar uno será las X y el jugador 2 será las O.")
    print("")

def verificarPosicion(respuestaUsuario, lista):
    if respuestaUsuario < 1 or respuestaUsuario > 9:
        print("Favor de ingresar un número entre el 1 y el 9.")
        return 0
    elif respuestaUsuario == 1 and lista[0] == "X" or respuestaUsuario == 1 and lista[0] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 2 and lista[1] == "X" or respuestaUsuario == 2 and lista[1] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 3 and lista[2] == "X" or respuestaUsuario == 3 and lista[2] == "2":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 4 and lista[3] == "X" or respuestaUsuario == 4 and lista[3] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 5 and lista[4] == "X" or respuestaUsuario == 5 and lista[4] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 6 and lista[5] == "X" or respuestaUsuario == 6 and lista[5] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 7 and lista[6] == "X" or respuestaUsuario == 7 and lista[6] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 8 and lista[7] == "X" or respuestaUsuario == 8 and lista[7] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    elif respuestaUsuario == 9 and lista[8] == "X" or respuestaUsuario == 9 and lista[8] == "O":
        print("Esta posición ya ha sido seleccionada, favor de seleccionar otra.")
        return 0
    else:
        return 1

def verificarGanador(lista):
    if lista[0] == "X" and lista[1] == "X" and lista [2] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[0] == "X" and lista[3] == "X" and lista[6] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[0] == "X" and lista[4] == "X" and lista[8] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[2] == "X" and lista[5] == "X" and lista[8] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[2] == "X" and lista[4] == "X" and lista[6] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[3] == "X" and lista[4] == "X" and lista[5] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[6] == "X" and lista[7] == "X" and lista[8] == "X":
        print("Ganador: jugador 1.")
        return 1
    elif lista[0] == "O" and lista[1] == "O" and lista [2] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[0] == "O" and lista[3] == "O" and lista[6] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[0] == "O" and lista[4] == "O" and lista[8] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[2] == "O" and lista[5] == "O" and lista[8] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[2] == "O" and lista[4] == "O" and lista[6] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[3] == "O" and lista[4] == "O" and lista[5] == "O":
        print("Ganador: jugador 2.")
        return 1
    elif lista[6] == "O" and lista[7] == "O" and lista[8] == "O":
        print("Ganador: jugador 2.")
        return 1
    else:
        return 0