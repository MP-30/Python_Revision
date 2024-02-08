mylist = [1,5,8,4]
myset = set()
# print(type(myset))

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

    
my_dog = Dog(breed='Huskie', name='Tomy', spots=True)
my_old_dog = Dog(breed='Germen', name='Sheferd', spots=False)
    
print(type(my_dog))
print("My_dog attributes: Breed={}, Name={}, Spots={}, Species={}".format(my_dog.breed, my_dog.name, my_dog.spots, my_dog.species))
print("My old Dog attributes: Breed={}, Name={}, Spots={}, Species={}".format(my_old_dog.breed, my_old_dog.name, my_old_dog.spots, my_dog.species))

    