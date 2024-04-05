'''QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.'''

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 0

test = {
    'input' :{
        'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 7
},
    'output' : 3
}

# locate_card(test['input']['query'], test['input']['query']) == test['output']
# or

def locate_card(cards,query):
    # Create a variable position with the value 0
    position = 0
    
    while True:
        if cards[position] == query:
            return position
        position +=1

        if position == len(cards):
            return -1

print (locate_card(cards,query))
# print(locate_card(**test['input'])== test['output'])

