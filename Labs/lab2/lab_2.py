

def main():
    print("Welcome to my PC management list, below are 4 Options:")
    

    # We'll have 4 parts
    # - Add
    # - Remove
    # - View parts
    # - Exit

    pcParts = []
    # try:
    while True:
        try:
            print("\n1. Add part\n"
                  "2. Remove part\n"
                  "3. View parts\n"
                  "4. Exit\n")

            userNum = int(input("Please choose an option (Number digits only): "))
            if userNum == 1:
                print("Great, now type the part you want to add: ")
                pcParts.append(input().lower())

            elif userNum == 2:
                print("Which part would you like to remove: ")
                pcParts.remove(input().lower())

            elif userNum == 3:
                print(f"Here's everything in your shopping cart:"
                      f"\n{pcParts}")

            elif userNum == 4:
                print("Thanks for visiting our website! Hope to see you again")
                break
        #It's very likely someone will mistype when removing a part (or sometimes it won't match)
        #So it's just here to prevent a hard stop and keep the loop going regardless
        except ValueError:
            print("Looks like you mistyped, please enter a valid input.")
            continue

    # except ValueError:
    #     print("Looks like you mistyped, wanna try again?\n")
    #     main()


    """
    If a user puts an extra space after they type the name of the part, 
    mine doesn't take into consideration to remove that spacing. Thing I'll have to prioritize 
    """
main()