a = [11, 12]
b = [21, 22]
c = [31, 32]

l1 = [a, b, c]
print(l1)

# Basically saying, go on the first list, and access the second index
print(l1[1][1])

# For this exercise, we'll add 10 to each element of a
for i in range(len(a)):
    a[i] = a[i] + 40

# # We'll do the same thing but for every list
# for i in range(len(l1)):
#     temp_list = l1[i]
#     # It's kinda confusing but j is is the inner index for the lists sinside
#     for j in range(len(temp_list)):
#         l1[i][j] = l1[i][j]+10
# print(l1)

# This is a more concise version of the code above
for i in range(len(l1)):
    for j in range(len(l1[i])):
        l1[i][j] = l1[i][j]+10
print(l1)


