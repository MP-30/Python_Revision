# Que_1: Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
for s in st.split():
  if s[0] == 's':
    print(s)
print("***********************")
# Que_2: Use range() to print all the even numbers from 0 to 10.

for i in range(0,10):
  if (i == 0):
    pass
  elif (i % 2 == 0):
    print(i)

# Que_3: Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

div_by_3 = [x for x in range(1,50) if x%3 ==0]

print(div_by_3)
print("*****************************")
# Que_4: Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
for x in st.split():
  if (len(x) % 2 ==0):
    print (x)
print("*************************")
# Que_5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,100):
  if num % 3 == 0 and num %5 == 0:
    print('FizzBuzz')
  elif num % 5 == 0:
    print('Buzz')
  elif num % 3 == 0:
    print('Fizz')
  else:
    print(num)
print("***************************")
# Que_6 Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
x = [i[0] for i in st.split()]
print(x)