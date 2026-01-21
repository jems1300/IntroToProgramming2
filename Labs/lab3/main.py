"""
A local company wants to provide wellness plans to members to maintain proper weight level.
For our in class assignment, we'll make a BMI calculator to rely on classes that both manage
and process the info. We'll make a Loan Class to construct objects that consist
- Loan amount
- Number of years The Loan will be taken
- Annual Interest rate on the loan
- The date the loan was taken out (we can use the import datetime)

"""
from Loan import Loan

b = Loan(50000, 10, 0.04)

print(f"The total student loan amount: ${b.getAmount()} was taken out on {b.dateTaken()}")
print(f"The loan will be taken out for {b.getYears()} year/s at an interest "
      f"rate for {b.getRate()*100}%")
print(f"The monthly payments will be ${round(b.getMonthly(), 2)}")
print(f"The total amount will be ${round(b.getTotal(), 2)}")
# def main():
#     print("hello")
# main()