# WARMUP SECTION:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5

print("Question 1")
def lesser(x,y):
  if x % 2 == 0 and y % 2 == 0:
    if x > y:
      print (y)
    else: print (x)
  elif x % 2 == 0 and y % 2 != 0:
    if x > y:
      print (x)
    else: print (y)
  elif x % 2 != 0 and y % 2 == 0:
    if x > y:
      print (x)
    else: print (y)
  elif x % 2 != 0 and y % 2 != 0:
    if x > y:
      print (x)
    else: print (y)
  else:
    print('You did some thing Wrong')

lesser(9,11)  

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

print("Question 2")
def two_words(x):
  y,z = x.split()
  if(y[0] == z [0]):
    print('True')
  else: print('False')
two_words('aha adi')
# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False
print("Question 3")
def twenty(x,y):
  if (x == 20 or y == 20 or x+y ==20):
    return True
  else:
    return False
print(twenty(619,1))

# LEVEL 1 PROBLEMS
# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

# Note: 'macdonald'.capitalize() returns 'Macdonald'

print("Question 3")
def cap(x):
  y = x[0].capitalize()
  z= x[3].capitalize()
  new_str1 = x.replace(x[0], y)
  new_str = new_str1.replace(x[4], z)
  print(new_str)
cap('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'

# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

print("Question 4")
def reverse(a):
  x = a.split()
  y = list(reversed(x))
  print(y)  
  
reverse('I am Aditya')

# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True

# NOTE: abs(num) returns the absolute value of a number
print("Question 5")
def with_in_10(x):
  int(x)
  if x in range(90,110):
    print(True)
  elif x in range(190,210):
    print(True)
  else: print(False)
with_in_10(209)

# LEVEL 2 PROBLEMS
# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

print("Question 6")
def find_33(a):
    b = len(a)
    for i in range(0,b-1):
      if a[i] == a [i+1] and a[i] == 3:
        return True
    else: return False
    
  
  
print(find_33([3,1,2,3,4,5,3]))
  
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

print("Question 7")
def repeat(str):
  b = ''
  for i in range(0,len(str)):
    result = str[i] *3
    b = b + (result)
  print (b)
    
repeat('aditaysingh')
  

# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19
print("Question 7")

def three_int(x,y,z):
  if (x+y+z <= 21):
    return x+y+z
  
  elif (x+y+z > 21 and (x == 11 or y == 11 or z == 11)):
    if ((x+y+z)-10) > 21:
      return 'BUST'
    else:
      return ((x+y+z)-10)
  elif (x+y+z > 21):
      return 'BUST'
  
print(three_int(9,9,11))
    
    



# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

print ("Question 8")
def Sixty9(a):
  j = k = -1
  for i in range (len(a)):
    if (a[i] == 6):
      j = i
    elif (a[i] == 9):
      k = i
  print("j" + str(j))
  if i == -1 or k == -1:
    print("6 and 9 not found in list")
    return
  print("j:",j)
  print("k:",k)
  e = sum(a[0:j])
  f = sum (a[k+1:])
  print("total", e + f)    
Sixty9([2, 1, 6, 9, 11])
# CHALLENGING PROBLEMS
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False
print ("Question 9 not done")
'''
Wrong solution
def zero7(lists):
  i = {}
  for a in range(len(lists)):
    if lists[a] == 0:
      i[a]= lists[a]
    elif lists[a] == 7:
      i[a]= lists[a]  
  if len(i)>=3:
      
      key = i.keys()
      list_of_key = (list(key))
      print(list_of_key)
      print(list_of_key[0])
      if list_of_key[0] < list_of_key[1] < list_of_key[2]:
        print(True)
      else: return False       
    
zero7([1,7,2,0,4,5,0])
'''
def spy_game(nums):
  code = [0,0,7,5]
  for num in nums:
    if num == code[0]:
      code.pop(0)
  return len(code) == 1
print(spy_game([1,7,2,0,4,5,0]))
 
#  COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25


# By convention, 0 and 1 are not prime.
print("Question 10")
'''
wrong solution
def prime(num):
  b = 0 
  for i in range (2, num):
    if num % i== 0: 
       b = 1 
       break
      
    else: print(i)
  
prime(73)
'''
def count_primes(nums):
  if nums <2:
    return 0
  primes = [2]
  x = 3
  while x <= nums:
    for u in range(3,x,2):
      if x % u == 0:
        x += 2
        break
    else:
      primes.append(x)
      x += 2
  print(primes)
  print(len(primes))
count_primes(100)
# ust for fun:
# PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
# print_big('a')

# out:   *  
#       * *
#      *****
#      *   *
#      *   *
# HINT: Consider making a dictionary of possible patterns, and mapping the alphabet to specific 5-line combinations of patterns.
# For purposes of this exercise, it's ok if your dictionary stops at "E".