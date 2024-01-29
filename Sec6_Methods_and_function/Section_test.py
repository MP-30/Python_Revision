# Functions #1: print Hello World
# Write a function called myfunc that prints the string 'Hello World'.

def hello():
  print("Hello World")
hello()

# Functions #2: print Hello Name
# Define a function called myfunc that takes in a name, and prints 'Hello Name' 



# Also, do not use f-strings, as they are not supported in this Coding Exercise.

def hello_name(name):
  print(f'Hello {name}')
hello_name('Aditya')

# Functions #3 - simple Boolean
# Define a function called myfunc that takes in a Boolean value (True or False). If True, return 'Hello', and if False, return 'Goodbye'

def boole(inputs):
  if inputs == True:
    return('Hello')
  elif inputs == False:
    return ('Goodbye')
  
print(boole(False))

# Functions #4 - using Booleans
# Define a function called myfunc that takes three arguments, x, y and z.
# If z is True, return x.  If z is False, return y.

def fun(x,y,z):
  if z == True:
    return x
  elif z == False:
    return y
print(fun('aditya', 'singh', False))


# Functions #5: simple math
# Define a function called myfunc that takes in two arguments and returns their sum.

def sum (x,y):
  return(x+y)
print(sum(5,7))


# Functions #6: is even
# Define a function called is_even that takes in one argument, and returns True if the passed-in value is even, False if it is not.

def is_even(x):
  if x %2 == 0:
    return (f'{x} is even')
  elif x %2 != 0:
    return (f'{x} is odd')
  
print(is_even(8))


# Functions #7: is greater
# Define a function called is_greater that takes in two arguments, and returns True if the first value is greater than the second, False if it is less than or equal to the second.

def is_greater(x,y):
  if x > y: 
    return True
  elif x <= y:
    return False
print(is_greater(99,89))

# Functions #8: *args
# Define a function called myfunc that takes in an arbitrary number of arguments, and returns the sum of those arguments.

def myfun(*args):
  a = 0
  for i in args:
    a = a+ i
  print(a)
    
myfun(4,8,9,7,5,3,6,9,8,5,2,1)


# Functions #9: pick evens
# Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only those arguments that are even.

def myfunc(*args):
  result = []
  for i in args:
    if i % 2 == 0:
      result.append(i)
  return (result)
  
  
print(myfunc(4,8,5,9,6,2,5,7,1,5,3))


# Functions #10: skyline
# Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.



def myfunc(string):
  a =''
  for x in range (len(string)):
      if (x+1) % 2 == 0:
        a = a + string[x].upper()
      else:
        a = a + string[x].lower() 
  return a
print(myfunc('aditya'))
   