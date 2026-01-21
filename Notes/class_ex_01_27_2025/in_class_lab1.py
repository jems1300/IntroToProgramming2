def main():

    dist = float(input("For this trip, what's the distance that you're travelling? "))
    days = int(input("Number of days of commute each week: "))
    mpg = float(input("Miles per gallon for the car: "))
    gasprice = float(input("Price per gallon: "))


    #This is preferable instead of having multiple if statements

    #Another way to write is that dist needs to be between 0 and 100
    #Like "if 0 < dist <= 100"
    if (dist>=0 and dist<= 100) and \
        (days>=0 and days<=7) and \
        (mpg>=1 and mpg<=200) and \
        (gasprice>=0 and gasprice<=10):
        print("Good")
    else:
        print("Input is invalid")

    if not 0<=dist<= 100:
        print("Input distance is invalid")
    elif not 0<= days <= 7:
        print("Input is invalid")
        #repeat for the others


    # commute distance: >= 0, <= 100
    # days of commute: >= 0, <= 7
    # miles per gallon: >= 1, <= 200
    # gas price: >= 0, <= 10


    #This code works, but it's flawed. There's a better way to improve it
    # if dist>=0 and dist<= 100:
    #     if days>=0 and days<=7:
    #         if mpg>=1 and mpg<=200:
    #             if gasprice>=0 and gasprice<=10:
    #                 print("Input is invalid")
    #             else:
    #                 print("Input is invalid")
    #         else:
    #             print("Input is invalid")
    #     else:
    #         print("Input is invalid")
    # else:
    #     print("Input is invalid")

    #There's a way to combine all of them in one line dummy
    # if 0 < dist <= 100:
    #     print("Input is invalid")
    # if 0 <= days <= 7:
    #     print("Input is invalid")
    # if 1 <= mpg <= 200:
    #     print("Input is invalid")
    # if 0 <= gasprice <= 10:
    #     print("Input is invalid")



main()