# In case you don't know how many inputs you're to take, a while loop is useful
max_num = -99999999999
cnt = -1
while True:
    num = int(input("Enter an integer. Enter 0 to stop"))

    if num == 0:
        break

    # Compare the what the user puts into in what is inside the list
    if num>max_num:
        max_num = num
        cnt = 1
    elif num == max_num:
        cnt = cnt+1
    else:
        continue

if max_num>0:
    print(max_num, cnt)
else:
    print("The user hasn't entered any number")