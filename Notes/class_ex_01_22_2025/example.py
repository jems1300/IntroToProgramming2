import random


def main():
    total = 0
    for count in range(1, 11):
        numbers = random.randrange(1, 11)
        print(numbers)
        total += numbers
    print(f"The sum of the numbers is {total}")


main()
