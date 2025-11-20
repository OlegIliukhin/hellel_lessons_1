class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.get_square() == other.get_square()

    @staticmethod
    def from_square(square: int):
        return Rectangle(1, square)

    def __add__(self, other):
        new_square = self.get_square() + other.get_square()
        return Rectangle.from_square(new_square)

    def __mul__(self, n: int):
        new_square = self.get_square() * n
        return Rectangle.from_square(new_square)

    def __str__(self):
        return f"Rectangle({self.width}x{self.height}), square={self.get_square()}"
