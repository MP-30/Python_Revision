def func():
    return 1
def hello(name = 'Jose'):
    print ('The hello() function has been executed')

    def greet():
        return '\t This is the greet() function inside hello!'
    print (greet())
hello()