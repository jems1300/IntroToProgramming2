# import math
# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def getX(self):
#         return self.__x
#
#     def getY(self):
#         return self.__y
#
#     def isNearBy(self, p1):
#         dist = math.sqrt( (self.getX() - self.getY())**2 + (self.getX() - self.getX())**2 )
#         print(dist)
#         if dist <= 5:
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return "(" + str(self.getX()) + "," + str(self.getY()) + ")" + " Is it near by? " + str(self.isNearBy(p1))
#
#
# p1 = Point(1, 8)
# print(p1)

class Account:
    def __init__(self, id=00000000, balance=100.0, annual_interest_rate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate


    def getID(self):
        return self.__id

    def getbalance(self):
        return self.__balance

    def getRate(self):
        return self.__annual_interest_rate

    def withdraw(self):
        user = float(input("Please enter the amount you would like to withdraw: "))
        return f"You've withdrawn ${user}, this is the remaining balance $", self.getbalance() - user

    def deposit(self):
        user = float(input("Please enter the amount you would like to deposit: "))
        return self.getbalance() + user


customer = Account()
print(customer.getbalance())
print(customer.withdraw())


