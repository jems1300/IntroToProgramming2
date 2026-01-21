from Shape import Shape

class Square(Shape):
    def __init__(self, x, y, edge_length):
        super().__init__(x, y)
        self.edge_length = edge_length
        # Square has the same lengths on all sides

    def area(self):
        return self.edge_length**2