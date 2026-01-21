# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding numbers
#   - The Fibonacci series begins with 0 and 1
#   - Each subsequent number is the sum of the preceding two.
#
#   - How many times is the factorial method invoked for factorial(6)
# I would say 5 times
#

# def x_method(n: int):
#     if n > 0:
#         print(n % 10)
#         x_method(n // 10)
#
#     def main():
#         x_method(1234567)
#
#     main()
#

# Checking Palindrome
# Non-recursive solution
# amanaplanacanalpanama

test_case = "madam"
low = 0
high = len(test_case)-1

is_palindrome = True
while (low < high):
    if test_case[low] == test_case[high]:
        low += 1
        high -= 1
    else:
        is_palindrome = False


'''
test_case = "madam"

def check_non_recursive(test_case):
    low = 0
    high = len(test_case) - 1

    is_palindrome = True
    while (low < high):
        if test_case[low] == test_case[high]:
            low += 1
            high -= 1
        else:
            is_palindrome = False
            break

test_case = "hanah"
print(check_non_recursive(test_case))

def check(test_case):
    if len(test_case)<=1:
        return True
    elif test_case[0] != test_case[-1]:
        return False
    else:
        check(test_case[1:-1])

test_case = "hanah"
print(check(test_case))
'''