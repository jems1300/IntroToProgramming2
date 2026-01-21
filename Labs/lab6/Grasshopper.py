from Bug import Bug


class Grasshopper(Bug):
    def __init__(self, name="Grasshopper", num_legs=6, num_wings=4):
        super().__init__(name, num_legs, num_wings)

    def jump(self):
        return f"This {self.get_name()} jumped"

    def sound(self):
        return f"This {self.get_name()} makes a chirping noise"
