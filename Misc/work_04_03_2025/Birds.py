from abc import abstractmethod

class Birds:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return f"This is a {self.get_name()}."

    @abstractmethod
    def eat(self):
        return f"This {self.get_name()} eats the food"