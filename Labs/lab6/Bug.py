class Bug:
    def __init__(self, name, num_legs=0, num_wings=0):
        self.name = name
        self.num_legs = num_legs
        self.num_wings = num_wings

    # Include methods to access or modify these properties

    def get_name(self):
        return self.name

    def get_legs(self):
        return self.num_legs

    def get_wings(self):
        return self.num_wings

    def __str__(self):
        return (f"This bug is named {self.get_name()} and has "
                f"{self.get_legs()} leg/s and {self.get_wings()} wing/s")
