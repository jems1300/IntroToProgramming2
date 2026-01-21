from Shape import Shape
class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length

    def get_length(self):
        return self.length

    def get_width(self):
        return self.width