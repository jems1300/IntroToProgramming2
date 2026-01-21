"""
You want to buy computer parts and want to keep a record of the both the parts and respective price.
We'll basically have to make a list where we'll be able to add, remove and view selected pars

- Lists
- Functions

For this In-Class, we'll be doing the management of the parts list.
"""


def main():
    print("Welcome to our management list, enter values down below\n"
          "Once you're done, please enter '-1'\n")

    l1 = []
    while True:
        grade = int(input("Please enter a value: "))
        l1.append(grade)
        if grade == -1:
            break

    # I added the pop, so I can get rid of -1, that way it doesn't show up on the print
    # And average the whole list without -1
    l1.pop()
    print(f"This is the list {l1}")
    l1avg = sum(l1) / len(l1)
    print(f"Your average is {l1avg}")


main()
