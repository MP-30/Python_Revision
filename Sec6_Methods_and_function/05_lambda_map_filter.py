def square(num):
    return num**2
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)
print(list(map(square, my_nums)))

def splicer(mystring):
    if len (mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['Aditya','Rohit','Vivek', 'Rama']
print(list(map(splicer, names)))

#filters

def check_even(num):
    return num % 2 == 0
my_num = [1,2,3,4,5,6,7,8,9]
print(list(filter(check_even, my_num)))
for n in filter(check_even, my_num):
    print(n)
    
    
# lambda 
square = lambda num: num **2
print(square(3)) 

print(list(map(lambda num: num**2, my_num)))
    
# filters

print(list(filter(lambda num:num % 2 == 0, my_num)))

print(list(map(lambda x:x[::-1],names)))
    
    
    