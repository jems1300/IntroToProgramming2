import math
import datetime

class Loan:
    def __init__(self, amount, years, rate):
        self.amount = amount
        self.years = years
        self.rate = rate
        self.date = datetime.date.today()


    def getAmount(self):
        return self.amount

    def getYears(self):
        return self.years

    def getRate(self):
        return self.rate

    def dateTaken(self):
        return self.date

    def getMonthly(self):
        monthlyRate = self.rate / 12
        # Make sure to include * as I got a type error when multiplying between parenthesis
        return ((self.amount * monthlyRate * (1 + monthlyRate) ** (self.years * 12)) /
                (1 + monthlyRate)**(self.years * 12 - 1))

    def getTotal(self):
        return self.getMonthly() * self.years * 12

