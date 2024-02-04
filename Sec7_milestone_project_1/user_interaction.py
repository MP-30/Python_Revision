game_list = [0,1,2]
def display_game(game_list):
    print("Here is the current lsit: ")
    print(game_list)
display_game(game_list)

def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("Pick a position (0,1,2): ")
        if choice not in ['0','1','2']:
            print("Sorry invalid choice! ")
            
    return int(choice)
print(position_choice())

def replacement_choice (game_list,position):
    user_palcement = input("Type a string to place at position: ")
    game_list[position] = user_palcement
    return game_list
print(replacement_choice(game_list, 1))

def gameon_choice():
    choice = 'wrong'
    while choice not in ['Y', 'N']:
        choice = input("Keep playing (Y and N)?")
        if choice not in ['Y', 'N']:
            print("Sorry! I don't understand, please choose Y or N")
    if choice == 'Y':
        return True
    else:
        return False
            
print(gameon_choice())

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)
    position = position_choice()
    game_list = replacement_choice(game_list,position)
    display_game(game_list)
    game_on = gameon_choice()
    