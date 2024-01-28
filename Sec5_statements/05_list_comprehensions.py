mystring = 'hello'
mylist = []
for letter in mystring:
  mylist.append(letter)
print(mylist)

#second way
mylist1 = [letter for letter in mystring]

print(mylist1)

mylist2 = [x for x in 'wordlist']
print(mylist2)

mylist3 = [x*x for x in range(0,11)]
print(mylist3)

mylist4 = [x for x in range(0,11) if x%2 ==0]
print(mylist4)

celcius = [0,12,45,89,570,568.3]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

fahrenheit1 = []
for temp in celcius:
  fahrenheit1.append((9/5)*temp + 32)
print(f'fahrenheit1 again: {fahrenheit1}')

results = [x if x%2 ==0 else 'ODD' for x in range(0,11)]
print(results)

mylist5 = []
for x in [2,4,6]:
  for y in [100,200,300]:
    mylist5.append(x*y)
print(mylist5)
mylist6 = [x*y for x in [2,4,6] for y in [10,523,785]]
print(mylist6)