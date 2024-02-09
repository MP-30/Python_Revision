class Animal():
    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print("I am a animal")
        
    def eat(self):
        print("I am eating")
        
my_animal = Animal()
print(my_animal.who_am_i())
print(my_animal.eat())

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created ")
    
    def eat(self):
        print("I am dog and eating")
        
    def who_am_i(self):
        print("I am a dog")
        
mydog = Dog()
mydog.who_am_i()
mydog.eat()
