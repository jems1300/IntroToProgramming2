# def main():
#     nums = [3, 7, 2, 1]
#     print(len(nums))
#     print(nums[-1])
#     # print(nums[len(nums)])
#     # There is an IndexError on line 5, try to see why that is the case
# main()

def loop():
    aList = [14, 55, 4, 34, 2, -3, 76]
    #         0   1  2   3  4   5   6
    index = 0
    for i in range(1, len(aList)):
        if (aList[i] < aList[index]):
            index = i

    print(index)
loop()

# This loops works as this, as it finds the index of the smallest element inside the list.
# The index starts a 0 -> "14" and assumes it's the smallest value. After that, it goes
# sequentially, and then finds the 2nd smallest number (smaller than 14), and it keeps going. After it
# goes through the entire list, it prints out the INDEX on where it stopped (-3 == 5)

def loop2():

    listA = [-8, 3, 45, 22, 12, 85]

    for i in range(1, 6):
        listA[i - 1] = listA[i]*2
    for i in range(0, 6):
        print(listA[i])

"""
This one is kinda weird, is like a weird trolley where it starts at position 1, but it goes back, so once it's 
multiplied by 2, that outcome replaces the previous index 
"""
loop2()

def loop3():
    myList = [-85, 34, 23, 90, 123]  # List of numbers
    maximumValue = myList[0]  # Start by assuming the first number is the largest
    indexOfMax = 0  # Store the index of the largest number (initially 0)

    for i in range(1, len(myList)):  # Loop through the rest of the list (starting at index 1)
        if myList[i] > maximumValue:  # If we find a bigger number...
            maximumValue = myList[i]  # Update the largest number
            indexOfMax = i  # Update the index of the largest number

    print(indexOfMax)  # Print the index of the largest number

loop3()

