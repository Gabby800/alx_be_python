# polymorphism_demo.py

import math

# Base class - Shape
class Shape:
    def area(self):
        # This method is meant to be overridden in subclasses
        raise NotImplementedError("Subclasses must override the area() method")


# Derived class - Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Calculate area for rectangle: length × width
        return self.length * self.width


# Derived class - Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Calculate area for circle: π × r²
        return math.pi * (self.radius ** 2)
