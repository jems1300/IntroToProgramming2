'''
The program will keep generating random addition
or subtraction questions and provide feedback to students until
students enter “quit.”
'''
import random


def main():
    print("Enter 'quit' to quit the quiz")
    while True:
        rand_num = random.randint(0, 9)
        rand_num2 = random.randint(0, 9)
        '''
        Since we're making this program for first graders, we don't want to introduce
        negative numbers. This is in place to prevent that by making sure the 2nd number is not
        bigger than the 1st number 
        '''
        if rand_num < rand_num2:
            # if the 1st num is less than the 2nd
            temp = rand_num
            rand_num = rand_num2
            rand_num2 = temp

        question1 = f"What does {rand_num}  + {rand_num2} equal to?: "
        question2 = f"What does {rand_num} - {rand_num2} equal to?: "

        questions = (question1, question2)

        # fix
        current_question = random.choice(questions)

        answer = input(current_question)
        if answer == "quit" or answer == "Quit":
            break
        answer = int(answer)

        if current_question == question1:
            if answer == rand_num + rand_num2:
                print("nice")
            else:
                print("wrong, try again")
        if current_question == question2:
            if answer == rand_num - rand_num2:
                print("nice")
            else:
                print("wrong, try again")
        # questions = input("Please enter your answer ")


main()
