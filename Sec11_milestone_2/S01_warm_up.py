import random
# Card class
# suit, rank, value, 
values = {'Two':2, 'Three':3, 'Four':4, 'Five': 5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack': 11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight','Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

# Deck

# Player

class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
    
two_hearts = Card("Hearts", "Two")
two_leaf = Card("Leaf", "Two")
three_of_clubs = Card("Clubs", "Three")

print(two_hearts.suit)
print(two_hearts.rank)
print(three_of_clubs.rank)

print(values[three_of_clubs.rank])
print(values[two_hearts.rank])
print(values[two_leaf.rank])

print(two_hearts.value < three_of_clubs.value)
print(two_hearts.value)