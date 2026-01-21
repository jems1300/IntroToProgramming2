import random
def compare_two_int(num1, num2):
    if num1>num2:
        print(str(num1) + ">" + str(num2))
    elif num1==num2:
        print(str(num1) + "==" + str(num2))
    else:
        print(str(num1) + "<" + str(num2))

def sort_two_int(num1, num2):
    if num1>num2:
        temp = num1
        num1 = num2
        num2 = temp

def give_me_a_num():
    print(random.randint)

def main():
    print("this is the main function")
    # compare_two_int(10, 5)
    # give_me_a_num()

    num1 =10
    num2 = 5

    num1, num2 = sort_two_int(num1, num2)

main()