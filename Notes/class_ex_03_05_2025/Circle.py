import math
from Shape import Shape
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        # super means the super class, like the parent class
        # By doing this, we inherit the variable and method from Shape
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def super_area(self):
        super().area()
