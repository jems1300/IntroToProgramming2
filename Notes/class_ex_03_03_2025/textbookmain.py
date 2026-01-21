from textbook_examples2 import Circle

def main():
    x = float(input())
    y = float(input())
    radius = float(input())

    c = Circle(x, y, radius)

    print(c.x, c.y, c.radius)

main()