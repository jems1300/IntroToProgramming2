# class Circle:
#     def __init__(self, x, y, radius):
#         self.x = x
#         self.y = y
#         self.radius = radius
#
#     def x(self):
#         return self.x
#
#     def y(self):
#         return self.y
#
#     def radius(self):
#         return self.radius
#
# def main():
#     x = float(input())
#     y = float(input())
#     radius = float(input())
#
#     c = Circle(x, y, radius)
#
#     print(c.x, c.y, c.radius)
#
# main()


class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "(" + str(self.width) + ", " + str(self.height) + "):" + str(self.height * self.width)

def main():
    for i in range(3, 7):
        r = rectangle(i, i+2)
        print(r)

main()

class rectangle2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __eq__(r1, r2):
        return (r1.width == r2.width and r1.height == r2.height) or \
               (r1.width == r2.height and r1.height == r2.width)

def main2():
    r1 = rectangle2(float(input()), float(input()))
    r2 = rectangle2(float(input()), float(input()))

    print(r1 == r2)

main2()

# def main():
#     objTimer = Timer(100)
#     timer = 100
#     for i in range(0, 100):
#         tickInt(timer)
#         tickTimer(objTimer)
#     print("objTimer =", objTimer.time, "timer =", timer)
#
# def tickTimer(t):
#     t.time -= 1
#
# def tickInt(timer):
#     timer -= 1
#
# class Timer:
#     def __init__(self, time):
#         self.time = time
#
# main()