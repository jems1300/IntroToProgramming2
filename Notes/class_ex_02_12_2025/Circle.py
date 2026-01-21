import math

class Circle:
    # new_radius is a placeholder so we can pass the data
    def __init__(self, new_color=None, new_radius=1):
        # Initializer
        # Used to initialize the state of a new object and use constructors
        self.radius = new_radius
        self.color = new_color



        # Methods
    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def setRadius(self, new_radius):
        self.radius = new_radius

    def setColor(self, color):
        self.color = color