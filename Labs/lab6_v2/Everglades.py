from Exhibit import Exhibit

class Everglades(Exhibit):
    def __init__(self, name = "everglades", temp = 80, humidity = 90):
        super().__init__(name, temp, humidity)
        self.water_lvl = 5


    def get_water(self):
        return self.water_lvl

    def __str__(self):
        return (f"This is a(n) {self.get_name()}\n"
                f"The temperature is {self.get_temp()} degrees Fahrenheit\n"
                f"The humidity is {self.get_hum()}\n"
                f"The water level is {self.get_water()}\n")
