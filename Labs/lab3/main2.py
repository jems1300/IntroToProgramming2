from BMI import BMI

member = BMI("Josh", 160, 66, 2000)
member2 = BMI("Jane", 123, 64, 1998)

member.setWeight(145)

print(f"The BMI for {member.getName()} (Age: {member.calcAge()}) is {round(member.calcBMI(), 2)} "
      f"<=== {member.typeBMI()}")
print(f"The BMI is {member2.getName()} (Age: {member2.calcAge()}) is {round(member2.calcBMI(), 2)} "
      f"<=== {member2.typeBMI()}")