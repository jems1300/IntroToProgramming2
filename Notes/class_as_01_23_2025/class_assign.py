"""
Key things
We'll make a program that'll keep generating random questions
double-check the answers, let the lil guys know if they were right or wrong
then keep on going on that loop until they decide to quit

author: JONATHAN MEDINA
date: 1/23/2025
"""

import random


def main():
    print("Welcome to my Math Quiz! At any time, type 'Quit' to stop Quiz.\n")

    correct_answers = 0
    total_count = 0
    # I left them outside here because inside the loop they were inactive

    while True:
        rand_num1 = random.randint(0, 9)
        rand_num2 = random.randint(0, 9)

        # I don't want Num2 being bigger than Num1
        if rand_num2 > rand_num1:
            temp = rand_num1
            rand_num1 = rand_num2
            rand_num2 = temp
        # we'll store 2 into a temp value so we don't get negative numbers

        question1 = f"What does {rand_num1} - {rand_num2} = ?\n"
        question2 = f"What does {rand_num1} + {rand_num2} = ?\n"
        '''
        honestly the hardest part about this was figuring out how to randomly choose between adding/subtraction 
        earlier attempts it would just keep looping the same one >:( 
        '''

        # I made an error by typing random.choice(questions) within input(), but doing so it was always static
        # Essentially I forgot tuples were a thing. So I made another variable, current_question, to store whatever
        # actual random choice it went with from that lottery box
        questions = [question1, question2]
        current_question = random.choice(questions)

        answer = input(current_question)

        # I put a try block here in case they mistype, since it would just hard stop loop otherwise
        try:
            # If answer == "Quit" or "quit":
            if answer == "Quit" or answer == "quit":
                break
                # If they don't type quit, then input will be converted into an integer
            answer = int(answer)
            total_count += 1
            # I overcomplicated this step by trying to put into my if current question statements (which doubled my
            # count) but the simpler solution was to put it here. So everytime answer converted into an int, now it
            # would increment the total count regardless of which question it pulled.
        except ValueError:  # <- I looked at the exception error in the console, so it wouldn't be too broad as the
            # IDE warned me
            print("Oops, looks like you mistyped. Wanna try again?\n")
            continue
        # In case a mistake happens, give them a slap on the wrist and keep going

        '''
        I'd like to imagine of drawing out of a box, so if the current question equals 1, then it'll make sure that 
        it actually adds up together, and reinforce the user (or not) if they're on the right track    
        '''

        # If they got either question right (for adding/subtraction) it would increment the correct amount variable
        if current_question == question1:
            if answer == rand_num1 - rand_num2:
                print("Great Job!\n")
                correct_answers += 1
            else:
                print("Not quite, but try again!\n")

        if current_question == question2:
            if answer == rand_num1 + rand_num2:
                print("Great job!\n")
                correct_answers += 1
            else:
                print("Not quite, but try again!\n")

    print(f"You got {correct_answers} out of {total_count} question/s right")
    # print(f"You scored {round(correct_answers/total_count, 2) * 100}% on this quiz")
    total_grade = round(correct_answers / total_count, 2) * 100
    if total_grade > 70:
        print(f"You scored a {total_grade}% on this Quiz, congrats!")
    if total_grade < 70:
        print(f"You scored a {total_grade}% on this Quiz. No worries, study hard and come back next time!")
    # This wasn't necessary, but I thought it'd be fun to include


main()
