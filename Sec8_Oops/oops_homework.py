import math

# Problem1 : Find distance and slope b/w two cordinates
class line:
    def __init__(self, cor1,cor2):
        self.cor1 = cor1
        self.cor2 = cor2
    def distance(self):
        return (((self.cor1[0] - self.cor2[0])**2) - ((self.cor1[1] - self.cor2[1])**2))**0.5
    def slope(self):
        return ((self.cor2[0] - self.cor2[1]) / (self.cor1[0] - self.cor1[1]))
cordinate1 = (5,6)
cordinate2 = (9,4)

li = line(cordinate1, cordinate2)


print(f'Distance is {li.distance()}')
print(f'Slope is {li.slope()}')

# Problem2: 

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        return (math.pi * (self.radius ** 2) * self.height)
        
    def surface_area(self):
        return ( (2 * math.pi * (self.radius ** 2)) + 2 * math.pi * self.height )

radius = 3
height = 2
my_cyc = Cylinder(height, radius)

print('Volume of cylinder is {a} and surface area of cylinder is {b}'.format(a = my_cyc.volume(), b = my_cyc.surface_area()))