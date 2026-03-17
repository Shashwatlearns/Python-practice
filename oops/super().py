class Shape:
    def __init__(self, colour, is_filled):
        self.colour = colour
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.colour} and {'filled' if self.is_filled else 'unfilled'}.")


class Circle(Shape):
    def __init__(self, colour, is_filled, radius):
        super().__init__(colour, is_filled)
        self.radius = radius

    def describe(self):
        print(f"It is a circle of area {3.14*(self.radius**2)}.")
        super().describe()


class Square(Shape):
    def __init__(self, colour, is_filled, width):
        super().__init__(colour, is_filled)
        self.width = width


class Triangle(Shape):
    def __init__(self, colour, is_filled, width, height):
        super().__init__(colour, is_filled)
        self.width = width
        self.height = height


circle = Circle("black", True, 5)
square = Square("blue", True, 7)
triangle = Triangle("red", True, 10, 15)

print(circle.colour)
print(circle.is_filled)
print(circle.radius)

print(square.colour)
print(square.width)
print(square.is_filled)

print(triangle.colour)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)

circle.describe()
square.describe()
triangle.describe()

# In conclusion super() lets You use the methods and attributes from the parent even after making a new construct statement for the child.
# I saw 2 uses of it -
#                      1. Even if you have new attributes for the child class, you can still use attributes from the parent class.
#                      2. You can create a new method having the same or different name as in the parent class and still use the method from the parent class.

# Use super() when you have to add more/different attributes than the parent class otherwise, just use pass