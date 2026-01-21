# squareTriangle, which prints a triangle of squares based on parameter
def squareTriangle(num):
    for row in range(1, num + 1):
        for col in range(1, row):
            print(row * col, end="\t")

        print(row * row) # Remember indentation

squareTriangle(2)
squareTriangle(4)

