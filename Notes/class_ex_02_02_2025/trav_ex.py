'''
Given nums has been initialized as a list of integers from the user input, multiply all the values together.
Make sure you add an extra blank line at the end when testing it
'''
from operator import index

def p1():
    nums = []
    line = input()

    while line !='':
        nums.append(int(line))
        line = input()

    prod = 1
    # For every number in the list of nums, make it multiply each other
    for i in nums:
        prod *= i

    print(prod)
p1()



def p2():
    nums = []
    line = input()

    while line != '':
        nums.append(int(line))
        line = input()

    cnt =  0
    for i in nums:
        # Basically saying that for every index in the list, if that list is between 1 and 100, increase the cnt
        if 1 <= i <= 100:
            cnt += 1

    print(cnt)
p2()



def numOfSmaller(list1, target):
    num = 0
    for i in list1:
        if i <= target:
            num += 1
    return num

# For every index in list1, if it's smaller than the input that I put, then increase the cnt towards num

def main():
    print("This program will check which numbers are smaller than your target\n")
    target = float(input("Please enter you set target number: \n"))
    lst = list()
    val = float(input("Now enter your numbers: \n"))
    while val != 0:
        lst.append(val)
        val = float(input())

    print(f"There are {numOfSmaller(lst, target)} number/s smaller than {target}")

main()


"""
Ok so for this function, we got to count how many elements are smaller than the adjacent element on its left
so like given a list of [10, 1, 2, 7, 12], the result should be 1 because only 1 is smaller than 10 
(2 is not smaller than 2, 7 is not smaller 7, 12 is not smaller than 12 etc you get the gist) 
"""

def numOfSmallerThanLeft(list1):
    num = 0

    for i in range(1, len(list1)):
        leftValue = list1[i - 1]
        indexValue = list1[i]
        if indexValue < leftValue:
            num += 1

    return num

def main2():
    alist = list()

    while True:
        value = float(input())
        if value == 0:
            break
        else:
            alist.append(value)

    print(alist)
    print(numOfSmallerThanLeft(alist))

main2()