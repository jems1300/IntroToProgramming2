from Shape import Shape
from Color import Color

class FilledCircle(Shape, Color):
    def __init__(self, x, y, radius, color):
        super().__init__(color)
        self.radius = radius
