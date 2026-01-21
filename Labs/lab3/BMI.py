#Purpose. This is a measurement based on height and weight. We can calculate it by taking your
#weight in kilograms and dividing it by the square of your height in meters.

#We'll follow this
"""
BMI<18.5 = underweight
18.5 < BMI < 25.0 = Normal
25.0 < BMI < 30 = Overweight
30. 0 < BMI = Obese

name
age
weight (lb)
height (inches)
For the age, use the datetime library to compute the value
"""
import datetime

class BMI:
    def __init__(self, name, weight, height, birth_year):
        self.name = name
        self.weight = weight
        self.height = height
        self.birth_year = birth_year

    #All the 3 getters just return whatever associated value is stated
    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height

    def calcAge(self):
        today = datetime.date.today()
        return today.year - self.birth_year
        #I had originally tried subtracting with just today, but I had to specify with .year to say what exactly was
        #being subtracted
    def setWeight(self, weight):
        self.weight = weight

    def calcBMI(self):
        weight_kg = self.weight * 0.45359237
        height_m = self.height * 0.0254
        total = weight_kg / (height_m ** 2)
        return total
    #This function actually calculates their total BMI, from inputted weight and height (made sure to convert to kg and
    #and meters for each respectively

    def typeBMI(self):
        if self.calcBMI() < 18.5:
            return "Underweight"
        elif 18.5 < self.calcBMI() < 25.0:
             return "Normal"
        elif 25.0 < self.calcBMI() < 30.0:
            return "Overweight"
        elif 30.0 < self.calcBMI():
            return "Obese"
        #And then depending on where the BMI falls on the scale, it will give you a score