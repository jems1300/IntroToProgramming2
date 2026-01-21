from Circle2D import Circle2D
from Point import Point

def main():
    circle = Circle2D(0, 0, 2)
    print(circle.getArea())
    print(circle.getPerimeter())
    p1 = Point(1, 1)

    print(circle.containPoint(p1.getX(), p1.getY()))


main()