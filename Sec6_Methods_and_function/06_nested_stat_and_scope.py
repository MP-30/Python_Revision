x = 25
def printer():
    x = 50
    return x
print

# local scope
#lambda num:num*2 

# Enclosing function scope

#Global
name = 'This is a global string'

def greet():
    #Enclosing    
    name = 'Aditya'
    def hello():
        #Local
        name = "I am a local"
        print('Hello '+ name)
    hello()
greet()  

########
x = 50
def func():
    global x
    print(f'X is {x}')
    #local reassingment on a global variable!
    x = 'NEW VALUE'
    print(f'X is local {x}')
     
func()