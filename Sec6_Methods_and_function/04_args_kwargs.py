def myfun(a,b,c=0,d = 0, e = 0):
  # Returns 5% of the sum of a and b
  return sum((a,b,c,d,e)) * 0.05
print(myfun(45,87,100,49,78))


def myfun1 (*args):
  return sum (args) * 0.5
print(myfun1(45,78,3,98,50,154,45,78))


def myf(*uk):
  print(uk)
myf(4,5,8,9,7,5,3,'',4,)

# * is for tuples of values

# ** is for dict (key value pair)

def myfunc(**kwargs):
  print(kwargs)
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else: print('I did not find any fruit here')
  
myfunc(fruit = 'apple',veg = 'coc', name = 'ady')

def mufunct(*args, **kwargs):
  print('I would like {}{}'.format(args[0], kwargs['food']))
print(mufunct(10,20,30, fruit='orange', food='egg', animal='owl'))