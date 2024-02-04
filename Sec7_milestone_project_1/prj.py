def display (row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)
row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']

row2[1] = 'X'
display(row1, row2, row3)

# result = int(input("Please enter a value: "))
# position_index = int(input("Choose an index position: "))

def user_choice():
    choice= 'Wrong'
    accepted_value = range (0,11)
    within_range = False
    

    # Digit pr Within range
    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number(0-10): ")
        # Digit Check
        if choice.isdigit() == False:
            print("Sorry this is not a digit")
        # Range Check
        if choice.isdigit() == True:
            if int(choice) in accepted_value:
                within_range = True
            else :
                print("Out of range")
                within_range = False
    return int(choice)
 
print(user_choice())
