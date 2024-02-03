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
    choice = input("Please enter a number(0-10): ")
    return choice.isdigit()

print(user_choice())