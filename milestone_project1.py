# In this code I refer marker to 'X' or'O'.

#To display the 3*3 grid (game board)
def print_board(board):
    print('\n'*100)
    print('   |    |')
    print(board[7]+'  |  '+board[8]+' |  '+board[9])
    print('   |    |')
    print('-------------')
    print('   |    |')
    print(board[4]+'  |  '+board[5]+' |  '+board[6])
    print('   |    |')
    print('-------------')
    print('   |    |')
    print(board[1]+'  |  '+board[2]+' |  '+board[3])
    print('   |    |')

#Let the Player 1 select 'X' or 'O'
def select_sign():
    mark = '' 
    while not (mark == 'X' or mark == 'O'):
        mark = input("Player 1: Choose X or O")
    
    if mark == 'X':
        return ('X','O')
    else:
        return ('O','X')

#To randomly select the player who starts first.
from random import randint
def select_player():
    choice = randint(0,2)
    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#To place the marker at the desired position in the board.
def place_mark(board,position,mark):
    board[position]=mark

#This is a function that return True if there is space left on the board.
def space_check(board,position):
    return board[position]==' '

#This function asks for the position of the marker to be placed at in the board.    
def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
    
#To check if winning condition is satisfied    
def win_condition(board,mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or #The First row in the game board Horizontally.
            (board[4]==mark and board[5]==mark and board[6]==mark) or #The Second row       "           "
            (board[1]==mark and board[2]==mark and board[3]==mark) or #The Third row      "             "
            (board[7]==mark and board[4]==mark and board[1]==mark) or #The Leftmost row Vertically.
            (board[8]==mark and board[5]==mark and board[2]==mark) or #The Middle row  "    "
            (board[9]==mark and board[6]==mark and board[3]==mark) or #The rightmost row  "   "
            (board[7]==mark and board[5]==mark and board[3]==mark) or #The Diagonal across
            (board[9]==mark and board[5]==mark and board[1]==mark))   #  "    "    "    "

# It returns True if there's no space left on the board 
def full_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    
# Simply asking the player if he wanna play again or not.
def play_again():
    return input("Do you want to play again?").lower().startswith('y')
    
# Here is the main driver function of the game
print("  *****WELCOME TO THE TIC TAC TOE GAME*****  ")
while True:
    game_board = [' ']*10
    player1_marker,player2_marker = select_sign()
    choice = input("Are you ready to play").lower()
    if choice[0] == 'y':
        game_is_on = True
    turn = select_player()
    while game_is_on:
        if turn == 'Player 1':
            print_board(game_board)
            position = player_choice(game_board)
            place_mark(game_board,position,player1_marker)
            print_board(game_board)
            if win_condition(game_board,player1_marker):
                print("Congratulations Player 1, You won the Game...!!!")
                game_is_on = False
            elif full_check(game_board):
                print("It's a Draw.")
                game_is_on = False
            else:
                turn = 'Player 2'
        
        else:
            print_board(game_board)
            position = player_choice(game_board)
            place_mark(game_board,position,player2_marker)
            print_board(game_board)
            if win_condition(game_board,player2_marker):
                print("Congratulations Player 2, You won the Game...!!!")
                game_is_on = False
            elif full_check(game_board):
                print("It's a Draw.")
                game_is_on = False
            else:
                turn = 'Player 1'
    
    if not play_again():
        break
