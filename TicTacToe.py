def board():
    board = """
    Este sera nuestro tablero de juego
    
    
    
    1 | 2 | 3
    --|---|--
    4 | 5 | 6
    --|---|--
    7 | 8 | 9
    
    *Instrucciones:
    1. Insertar un numero entre 1 al 9 para elejir la posicion.
    2. Se tienen que llenar las 9 posiciones para terminar el juego.
    3. Usted iniciara el juego.
    """
    print(board)
board()

tic = {"1","2","3","4","5","6","7","8","9"}

#posibles soluciones Format or Concatenar
#yes_votes = 42_572_654
#no_votes = 43_132_495
#percentage = yes_votes / (yes_votes + no_votes)
#'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
#' 42572654 YES votes  49.67%'
def update():
    print("""
    Elige una posicion 
          
    {tic[0]} | {tic[1]} | {tic[2]}
    --|---|--
    {tic[3]} | {tic[4]} | {tic[5]}
    --|---|--
    {tic[6]} | {tic[7]} | {tic[8]}
    
          """)

while True:
    update()

