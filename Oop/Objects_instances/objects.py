class House:
    def __init__(self, price):
        self.price = price
        
        
class Backpack:
    def __init__(self, color, size):
        self.items = []
        self.color = color
        self.size = size
        
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

class Rectangle:
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

class Movie:
    def __init__(self, title, year, language, rating) -> None:
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating