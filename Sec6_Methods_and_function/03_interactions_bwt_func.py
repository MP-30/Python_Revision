example = [1,2,3,4,5,6,7,8,9]
from random import shuffle
shuffle(example)
print(example)

def suffle_list(mylist):
  shuffle(mylist)
  return mylist 
print(suffle_list(example))

mylist = ['','0','']
print(suffle_list(mylist))

def player_guess():
  guess=''
  while guess not in ['0','1','2']:
    guess = input("Enter your guess(b/w 0,1,2): ")
  return(int(guess))

def check_guess(mylist, guess):
  if mylist[guess] == 'O':
    print('Currect')
  else:
    print('Wrong guess!')
    print(mylist)
    
# Initial list
mylist = ['','O','']
# Shuffle list
mixedup_list = suffle_list(mylist)

#User guess
guess = player_guess()

#Check guess
check_guess(mixedup_list, guess)
  
