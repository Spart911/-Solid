class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side