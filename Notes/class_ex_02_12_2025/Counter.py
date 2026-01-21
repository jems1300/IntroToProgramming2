class Counter:
    def __init__(self, limit =100):
        self.counter = 0
        self.limit = 10

    def increment(self):
        if self.counter < self.limit:
            self.counter += 1
        else:
            print("The counter has reached it's limit")

    def decrement(self):
        if self.counter > 0:
            self.counter -= 1
        else:
            print("The counter cannot decrease any more.")

    def get_value(self):
        return self.counter