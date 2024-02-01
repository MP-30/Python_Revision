# Complete the following questions: ____ 
# 1. Write a function that computes the volume of a sphere given its radius.

# The volume of a sphere is given as ((4/3)* pi * r^3)
 
import math
def sphere(radius):
    result = ((4/3)* math.pi * (pow(radius,3)))
    return result
print(sphere(7))

# 2. Write a function that checks whether a number is in a given range (inclusive of high and low)

def inrange(num, low, high):
    if num in range(low, high+1):
        return True
    else: return False
print (inrange(10,1,9))

# 3. Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

# Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Expected Output : 
# No. of Upper case characters : 4
# No. of Lower case Characters : 33

# HINT: Two string methods that might prove useful: .isupper() and .islower()

print ("**Question3")
def calculate(str):
    a = 0
    b = 0
    for i in str:
        x = i.isupper()
        if (x == True):
            a += 1
        elif (x == False):
            b += 1  
    print(f'Number of Upper case characters is {a}')
    print('Number of Lower case characters is {}'.format(b))
calculate('Hello Mr. Rogers, how are you this fine Tuesday?')

# 4. Write a Python function that takes a list and returns a new list with unique elements of the first list.

# Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
print("Question 4")
def unique(input):
    new_list = []
    for i in input:
        if i in new_list:
            pass
        else: new_list.append(i)
    print(new_list)
unique([1,1,1,1,2,2,3,3,3,3,4,5])

# Write a Python function to multiply all the numbers in a list.

# Sample List : [1, 2, 3, -4]
# Expected Output : -24
print('Question 5')
def mult(z):
    a = 1
    for i in z:
        a = a * i
    print(a)
mult([1, 2, 3, -4])

# Write a Python function that checks whether a passed in string is palindrome or not.

# Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run. 
print('Question 6')
def palidrome(a):
    b = a[::-1]
    if a == b:
        print (True)
    else: print(False)
    print(a)
    print(b)
    
palidrome([1,3,2,3,1])   

       

# Write a Python function to check whether a string is pangram or not.

# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"
print('Question 7')
import string
def pangram(str1 , alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    str1 = str1.replace(' ','')
    str1 = str1.lower()
    str1 = set(str1)
    return str1 == alphaset

        
print(pangram("The quick brown fox jumps over the lazy dog"))