class Toy:
    def __init__(self, name=None):
        self.name = name

    def input_name(self):
        self.name = input("Please enter the name of your new toy: ")

    def get_name(self):
        return self.name


class ToyFactory:
    def __init__(self):
        self.head = 100
        self.body = 100
        self.arm = 200
        self.leg = 200
        self.worker = 5

    def count(self):
        return (f"There are {self.head} head parts, {self.body} body parts, "
                f"{self.arm} arm parts, {self.leg} leg parts left and {self.worker} worker/s left")

    def count_worker(self):
        return self.worker

    def fetch_parts(self):
        self.head -= 1
        self.body -= 1
        self.arm -= 2
        self.leg -= 2

    def make_package(self):
        new_toy = Toy()
        new_toy.input_name()
        new_package = Package()
        self.worker -= 1
        if self.worker < 0:
            return "Sorry, we're at capacity, please come back at another time"
        elif self.head and self.body <= 0 and self.arm and self.leg <= 0:
            return "We are out of parts, come back at another date"
        else:
            self.fetch_parts()
            if self.head and self.body <= 0 and self.arm and self.leg <= 0:
                return "We are out of parts, come back at another date"
            else:
                new_package.name_label()
                return f"{new_toy.get_name()} has been shipped to {new_package.access_label()}"


class Package:
    def __init__(self, label=None):
        self.label = label
        self.contents = Toy().get_name()

    def name_label(self):
        self.label = input("And where will this toy be shipped to: ")

    def access_label(self):
        return self.label

    def access_content(self):
        return f"The toy {self.contents} in inside this package"
