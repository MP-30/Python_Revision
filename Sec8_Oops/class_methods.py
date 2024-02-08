class Dog():
    # Class object attributes
    # Same for any instance of a class
    species = 'mammal'  
    def __init__(self,breed, name, spots):
        # Attributes
        # We take in argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print("Woof! My name is {a} and the number is {b}".format(a =self.name, b = number))
        
my_dog = Dog('Lab', 'Tommy', True)
print(type(my_dog))
print(my_dog.species)
my_dog.bark(78)

class Circle():
    # Class Object Attribute
    pi = 3.14
    
    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    def get_circumference(self):
        return (self.pi * (self.radius)*2)
    
my_circle = Circle(5)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
