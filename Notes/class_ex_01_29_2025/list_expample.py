def fun():
    # Global tends to introduce more issues from what I understand
    global b
    b = 3
    a = 2
    print(a)

    # This is an example on how the error occurs, this happens because 'a' is a local variable


# print(a)
fun()
print(b)

l1 = []  # <-- Empty List
l2 = list()  # <-- Empty List

#       0         1        2        3
c = ["red", "yellow", "blue", "white"]
#      -4        -3       -2       -1
# You could go either way to print an index element

# c = [0] # Look up how to
c.append("black")
c.insert(0, "BRUH")
n = [3, 4, 1, 10]

print(l1)
print(l2)
print(c)
print(n)
print(f"There are {len(c)} element/s in list C")

# This allows us to print a specific index from the list
print(c)
print(c[-1])

# This will give you error to add string and int together
# print(sum(c))
print(min(c))  # <-- Returns the smallest item within that list
l = c + n  # <-- You can add two lists together too!
print(l)

l.remove(3)
l.remove("black")  # <-- Self explanatory
print(l)
print("green" in l)  # <-- It's saying if this element is in the list or not, gives you either T or F
print(l.index("blue"))  # <-- Tells me what index number this element is in
print(l)

"""
Another built in function in Python is sorting 
"""

# n = n.sort()
# Sort is a function, and sort does NOT have a return vale, which is why you get NONE

n.sort()
n.reverse()

# How to sort a list in descending order
n = list(range(0, 20, 1))
print(n)

# n[0] = n[0]+2
# n[0] = n[1]+2


# Increase each element by 2
for i in range(0, len(n), 2):
    print(n[i])

#List slicing
n1 = n[2:8]
print(n1)

n = [1, 2, 3]
print("original n", n)

# What seems to be the rpoblem
n1 = n
print("original n1", n1)
n1[0] = 0
print("updated n1", n1)
print("print n again", n)

a = 1
b = 2
print(a, b)
b = 3
print(a, b)

# deep copy
# 1) create a new list
# 2) copying each element to the new list
# n2 = []
# for i in range(len(n)):
#     n2.append(n[i])
# n2 = n.copy()
n2 = list(n)
print("original n2", n2)
n2[0] = 0
print(n2)
print(n)