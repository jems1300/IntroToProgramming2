# Example below
'''
An abstract class is a parent class, they
contain abstract methods which are declared but
have no implementation. The only way to make it work
is with a subclass. Imagine in the sense
that the abstract class is the body of the vehicle
and subclass
'''
from abc import abstractmethod


class Crustacean:
    def __init__(self, name, num_legs=0, claw=False):
        self.name = name
        self.num_legs = num_legs
        self.claw = claw

    def get_name(self):
        return self.name

    def get_legs(self):
        return self.num_legs

    def get_claw(self):
        return self.claw

    def __str__(self):
        if self.get_claw():
            return f"This is a {self.get_name()}, it has {self.get_legs()} leg/s and has no claws"
        elif not self.get_claw():
            return f"This is a {self.get_name()}, it has {self.get_legs()} leg/s and has claws "

    @abstractmethod
    def swim(self):
        return f"The {self.get_name()} swims"