class Toy:
    def __init__(self, name=None):
        self.name = name
    def inputName(self):
        self.name = input("Please enter the name of your new toy: ")
    def getName(self):
        return self.name

class ToyFactory:
    def __init__(self):
        self.head = 100
        self.body = 100
        self.arm = 200
        self.leg = 200
        self.worker = 5
        #self.__ssn = snn is an example of a private variable


    def count(self):
        return (f"There are {self.head} head parts, {self.body} body parts, "
                f"{self.arm} arm parts, and {self.leg} leg parts left")

    def fetchParts(self):
        self.head -= 1
        self.body -= 1
        self.arm -= 2
        self.leg -= 2

    def makeToy(self):
        new_toy = Toy()
        new_toy.inputName()
        self.worker -= 1
        if self.worker < 0:
            return "Sorry, we're at capacity. Please come back at another time"
        elif self.head and self.body <= 0 and self.arm and self.leg <= 0:
            return "We are out out of parts, come back at another date"
        else:
            self.fetchParts()
            if self.head and self.body <= 0 and self.arm and self.leg <= 0:
                return "We are out out of parts, come back at another date"
            else:
                return f"Say hello to {new_toy.getName()}, your new toy!"
