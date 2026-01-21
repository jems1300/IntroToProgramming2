from abc import ABC
from Birds import Birds

class Penguins(Birds, ABC):
    def __init__(self, name = "Penguin"):
        super().__init__(name)

    def __str__(self):
        return (f"This is a {self.get_name()}. It can blend well into it's shadows, though its "
                f"camouflage gives it no tactical advantage whatsoever, that was some pretty good squeaking though\n"
                f"{self.fly()}\n"
                f"{self.eat()}\n"
                f"{self.swim()}\n")

    def fly(self):
        return f"This {self.get_name()} cannot fly"

    def eat(self):
        return f"This {self.get_name()} eats the souls of the damned."

    def swim(self):
        return f"This {self.get_name()} can swim up to 430 mph"