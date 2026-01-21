'''
This will simulate a guessing game, this program will emphasize the following concepts
- Selections
- Repetition

implement a for loop that generates 10 numbers,
then add it up all together

Created in 1/22/2025
- Jonathan Medina
'''

import random


def main():
    # I create an empty list
    list = []
    # All the numbers that I create in this for loop will add inside this list

    '''
    I'm accustomed to Java so my for loops in python are a bit rusty,
    there might have been some stuff in here that I could've done better 
    '''
    # Tells it to do this 10 times only
    for index in range(10):
        number = random.randint(0, 9)
        # I import random, so I can generate a random number for each variable
        if number == 10:
            # Once the index reaches 10, it breaks
            break
        list.append(number)
        # And like I said earlier, I added all numbers into the empty list
        print(number)

    # Then I can use the sum for the whole list :)
    print(f"The sum for all 10 numbers is {sum(list)}")


main()

'''
Professor's Version 
import random 
def main():
    total = 0 
    for count in range(1, 11):
        numbers = random.randrange(1,11)
        print(numbers)
        total += numbers
    print("The sum of the numbers is ") 
'''
