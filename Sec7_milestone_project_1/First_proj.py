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
