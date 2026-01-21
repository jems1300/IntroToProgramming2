class Exhibit:
    def __init__(self, name, temp, humidity):
        self.name = name
        self.temp = temp
        self.humidity = humidity

    def get_name(self):
        return self.name

    def get_temp(self):
        return self.temp

    def get_hum(self):
        return self.humidity

    def __str__(self):
        return (f"This is a(n) {self.get_name()}\n"
                f"The temperature is {self.get_temp()} degrees Fahrenheit\n"
                f"The humidity is {self.get_hum()}\n")
