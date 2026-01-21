import random


def main():
    """
    Ask the user to input a number from 1 to 100 and generate a random
    number from 1 to 100. Determine if the user’s input is too high, too low,
    or the number chosen by the program. If the user’s input is too high or
    too low, provide feedback to let the user know and repeat the request
    for the user to input a number from 1 to 100.

    If the user’s input is the number chosen by the program, end the game.
    Ask the user if they would like to play again. Repeat the game if the user
    enters ‘y’ and terminate the game otherwise
    """
    print("Welcome to my guessing game! Guess the correct number.")

    while True:
        try:
            rand_num = random.randint(0, 100)
            print(rand_num)  # <- Placeholder for testing purposes

            answer = int(input("Please enter a number from 1 to 100: \n"))

            if answer == rand_num:
                user_input = input("Congrats, you've guessed the right number.\n"
                                   "Do you wish to continue this game? Yes or No?\n ").lower()
                if user_input == "yes":
                    main()  # <- Call on the main function to tell it to continue if it does match
                    continue
                # elif user_input != "yes":
                #     input("I'm not sure what you typed? Can you try again?")
                elif user_input == "no":
                    break

                ''' I have an issue where if someone types "asdf" the program still continues. I'll 
                see if I can rectify this in my own time '''

            if answer > rand_num:
                print("You're too high")
            if answer < rand_num:
                print("You're too low!")
        except ValueError:
            print("Oops, looks like you mistyped, wanna try again?")
            continue


main()
