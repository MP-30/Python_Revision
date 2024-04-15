'''QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.'''

import unittest

def locate_card(cards,query):
    # Create a variable position with the value 0
    position = 0
    
    while True:
        if cards[position] == query:
            return position
        position +=1

        if position == len(cards):
            return -1

# print (locate_card(cards,query))
# print(locate_card(**test['input'])== test['output'])
class TestLocateCard(unittest.TestCase):
    def test_locate_card(self):
        tests = [
            {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
            {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
            {'input': {'cards': [6], 'query': 6}, 'output': 0},
            {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
            {'input': {'cards': [], 'query': 7}, 'output': -1},
            {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
            {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}, 'output': 2}
        ]
        
        for test in tests:
            with self.subTest(test=test):
                self.assertEqual(locate_card(**test['input']), test['output'])

if __name__ == '__main__':
    unittest.main()
