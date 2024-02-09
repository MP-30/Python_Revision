'''
class Dog():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says woof!"
    
class Cat():
    def __init__(self, name):
        self.name = name
    def speak(self):
        return self.name + " says meow!"

miko = Dog("miko")
felix = Cat("felix")

for pet in [miko, felix]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())
pet_speak(felix)
'''
class Animal():
    def __init__(self, name):
        self.name = name
    def speak (self):
        raise NotImplementedError("Subclass must implemeet this abstract method")
    
# my_animal = Animal('fred')
# print(my_animal.speak())
     
class Dog(Animal):
    def speak(self):
        return self.name + " Says woof!"
               
class Cat(Animal):
    def speak(self):
        return self.name + " Says meow!"

fido = Dog("Fido")
isis = Cat("isis")

print(fido.speak())
print(isis.speak())