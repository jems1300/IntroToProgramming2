# def rangeFilter(list1, lb, ub):
#     res = list()
#     res.insert(0, lb) # <- I used insert because no matter what, this is gonna be the lowest value
#     res.append(ub) # <- This inserts into the very end of our list which is useful since we don't know how large this list is
#
#     for i in list1:
#         if lb <= i <= ub:
#             res.append(i)
#             res.sort()
#
#     return res
#
# def main():
#     lb = float(input("Type the low value: "))
#     ub = float(input("Type the high value: "))
#     list1 = list()
#     val = float(input("Now enter your shit:\n"))
#     while val != 0:
#         list1.append(val)
#         val = float(input())
#
#     print(rangeFilter(list1, lb, ub))
# main()

def averageOfA(list1):

    try:
        avg = sum(list1) / len(list1)
        if avg >= 90:
            return avg
        else:
            return -95.0
    except ZeroDivisionError:
        print("Hey, you can't divide by zero dummy")
        main()



def main():
    list1 = list()
    val = float(input())

    while val != 0:
        list1.append(val)
        val = float(input())

    print(averageOfA(list1))

main()