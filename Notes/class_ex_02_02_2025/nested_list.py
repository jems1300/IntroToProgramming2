m = [[1, 1, 1, 1, 1],
     [2, 2, 2, 2, 2],
     [3, 3, 3, 3, 3]]


def mystery(mat):
    prod = 1
    for i in range(len(mat)):
        j = 0
        sum = 0
        while j < len(mat[i]):
            sum += mat[i][j]
            j += 1

        prod *= sum

    return prod


print(mystery(m))

# Ask someone to explain this to you cause I DONT.