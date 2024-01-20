a = 'hello'
print(a)
b = 'this is also string'
c = "I'm giong to run"
print('hello \nworld')
print(len('hello'))
e = "Hello World I am Aditya a python programer"
print(e[6])
print(e[-2])
print(e[2:6])
print(e[1:55:2])
print(e[::-1])

name = "Aditya"
#name[0] = "O"
last_letter = (name[1:])
print(last_letter)

x = "Hello World"
x = x + " It is beautiful outside"
x = x + " It is beautiful outside"
print(x)
letter = "z"
print(letter *45)
print(letter.upper())
ad = "Hello thos is a string"
print(ad.split('t'))

print('This is a string {}'.format('INSERTED'))
print('The {2} {0} {1}'.format('fox','brown', 'quick'))
print('The {b} {f} {f}'.format(f='fox',b='brown',q ='quick'))

result = 100/777
print(result)

print("The result was {r}".format(r=result))

print("The result was {r:10.7f}".format(r=result)) 
result1 = 23.689
print("The result was {r}".format(r=result1))

name = "Jose"
print('Hello, his name is {r}'.format(r=name))
print(f"Hello, his name is {name}")
name = "Sam"
age = 3
print(f"{name} is {age} years old.")