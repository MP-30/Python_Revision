# Prblm 1
# Handle the exception thrown by the code below by using try and except blocks.


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError: 
    print("This is a type error")


print("============")    
# Prblm 2  
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.'
try:
    x = 5
    y = 0

    z = x/y
except ZeroDivisionError: print("Please dont do these type of mistake")

finally: print("All Done")

print("============")
# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.


def for_int():
    while True:
        try:    
            inti = int(input("Please enter a digit for square: "))
            final_value = inti **2
        except: print ("Your value is incorrect")            
            
        else: 
            print ('Square of your value is: {final_value}')
            print ("Thanks")
            break
for_int()