'''
board = ['1','2','3','4','5','6','7','8','9']
marker = ''
player1 = ''
player2 = ''
player1_position = ''
player2_position = ''
def display_board(test_board):
    print (f' {test_board[0]} | {test_board[1]} | {test_board[2]} ')
    print (f'-----------')
    print (f' {test_board[3]} | {test_board[4]} | {test_board[5]} ')
    print (f'-----------')
    print (f' {test_board[6]} | {test_board[7]} | {test_board[8]} ')
    


def user_input():
    
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ')
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    elif player1 == 'O':
        player2 = 'X'
    
    
    return (player1, player2)      
# player1_marker, player2_marker = user_input()
# print(f'Player 2 marker is: {player2_marker} ')
def user_position():
    print (f' 1 | 2 | 3 ')
    print (f'-----------')
    print (f' 4 | 5 | 6 ')
    print (f'-----------')
    print (f' 7 | 8 | 9 ')
    player1_position = input('Please select a position for player1: ')
    player2_position = input('Please select a position for player2: ')
    return (player1_position , player2_position)
# print(user_position())

def update_value_inList():
    board[player1_position] = player1
    board[player1_position] = player2 
    
    
def check_result():
    if (board[0] == board [1] == board [2] 
        or board[3] == board [4] == board [5] 
        or board[6] == board [7] == board [8]
        or board[0] == board [3] == board [6]
        or board[1] == board [4] == board [7]
        or board[2] == board [5] == board [8]
        or board[0] == board [4] == board [8]
        or board[2] == board [4] == board [6]):
        return ('Somebody won')
    else: pass
def final_game():
    
'''
board = ['#','X','O','X','O','X','O','X','O','X']

from IPython.display import clear_output
 
def display_board(board):
    clear_output()
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print(f'{board[1]} | {board[2]} | {board[3]}')
display_board(board)

def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, Choose X or O: ')
        
    if marker == 'X':
        return ('X', 'O')
    elif marker == 'O':
        return ('O', 'X')
player1_marker, player2_marker = player_input()
def place_marker(board, marker, position):
    board[position] = marker
place_marker(board, '$',8)


def win_check(board , mark):
    # To check who win tic tac to
    # Check all rows and check to see if they all share the same marker?
    # Check all columns and check to see if they all share the same marker?
    # Check both diagonals and check to see if they all share the same marker?
    
    return (board[1] ==  board[2] == board[3] == mark) or(board[4] ==  board[5] == board[6] == mark) or (board[7] == board[8] == board[9] == mark) or (board[1] == board[4] == board[7] == mark) or (board[2] == board[5] == board[8] == mark) or (board[3] == board[6] == board[9] == mark) or (board[1] == board[5] == board[9] == mark) or (board[3] == board[5] == board[7] == mark) 
display_board(board)
print(win_check(board, 'X'))   
   
import random
def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1' 
    else:
        return 'Player 2'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for a in range(1,10):
        if space_check(board,a):
            return False
    # Board is full
    return True
def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a postion:(1-9): '))
    return position
        
def replay():
    replay_input = input("Want to play again:(Yes or No)")
    return replay_input == 'Yes'

# main function to run the game continuously and break it when replay
print('Welcome to tic tac toe')
while True:
    # set every thing(board, whos first, choose marker X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input('Ready to play? y or n: ')

    if play_game == 'y':
        game_on = True
    else: game_on = False
    
    while game_on:
        if turn == 'Player 1':
            display_board(the_board)
           
            position = player_choice(the_board)
           
            place_marker(the_board, player1_marker, position)
           
            if win_check(the_board,player1_marker):
               display_board(the_board)
               print("Player 1 won!!") 
               game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                else: turn = 'Player 2'
        else: 
            display_board(the_board)
           
            position = player_choice(the_board)
           
            place_marker(the_board, player2_marker, position)
           
            if win_check(the_board,player1_marker):
               display_board(the_board)
               print("Player 2 won!!") 
               game_on = False
            else: 
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Tie Game!")
                    break
                else: turn = 'Player 1'
    ## Game play
    
    ## playew one turn
    
    ## Player two turn
    
    
 
    if not replay():
        break   
