import math
class Circle2D:
    def __init__(self, x=0, y=0, radius=0):
        self.x = x
        self.y = y
        self.radius = radius

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getRadius(self):
        return self.radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * math.pi * self.radius

    #Revise
    def containPoint(self, x, y):
        if ((self.x - x) ** 2) + ((self.y - y) ** 2) <= self.radius ** 2:
             return True
        if ((x - self.x) ** 2) + ((y - self.y) ** 2) > self.radius ** 2:
             return False

    def contains(self, circle):
        distance = math.sqrt((self.x - circle.getX()))