# Do a program that'll aks someone to put a number
# Then we'll divided that number

# def main():
#
#     user = int(input("Enter a number please: "))
#
#     if user % 5 == 0 and user % 3 == 0:
#         print("Divisible by 5 and 3")
#     elif user % 3 ==0 and user % 5 != 0:
#         print("Divisible by 3")
#     elif user % 5 == 0 and user % 3 != 0:
#         print("Divisible by 5")
#     elif user % 5 != 0 and user % 3 != 0:
#         print("It's not divisible by either")
#
#
# main()

def main2():
    nums = []

    while True:
        user2 = int(input("Please enter some numbers: "))
        nums.append(user2)
        if user2 == 0:
            break

    print(nums)
    print(f"Here's the total sum: {sum(nums)}")
main2()