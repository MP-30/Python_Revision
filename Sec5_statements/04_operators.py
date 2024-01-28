mylist  = [1,2,3]
for num in range(0,10,2):
  print(num)
  
print ('***************')

word = 'abcdef'
for index,letter in enumerate(word):
  print(index)
  print(letter)
  print('\n')

print ('***************')

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = ['e','r','t','h']
z = zip(mylist1, mylist2, mylist3)
for item in z:
  print(item)
  
print(list(zip(mylist3, mylist1, mylist2)))

print('*******************')
print('x' in [1,2,3,4,5])

print ('a' in 'aditya')

print ('mykey' in {'mykey', 6985})
d = {'mykey': 345}
print(345 in d.values())


print('*******************')
mylist = [10,20,30,40,50,60]
print(min(mylist))
print (max(mylist))


from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9]
shuffle(mylist)
print(mylist)

from random import randint

print(randint(10,1000))

result =  input ('Enter your number')
print(result)
print(type(result))