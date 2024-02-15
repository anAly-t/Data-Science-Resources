# Exercise: Modeling a Geometric Shape Hierarchy:

# Create a base class for geometric shapes with methods for calculating area and perimeter.
# Derive subclasses for specific shapes like rectangles, circles, and triangles.
# Add methods to each subclass for computing their specific properties.
# Create instances of different shapes and test the methods.

import math

class GeometricShape:
    def __init__(self):
        """
        Initialize a generic geometric shape.
        """
        pass  # No specific attributes for the base class

    def calculate_area(self):
        """
        Calculate the area of the geometric shape.
        """
        raise NotImplementedError("Subclasses must implement the calculate_area method.")

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the geometric shape.
        """
        raise NotImplementedError("Subclasses must implement the calculate_perimeter method.")

class Rectangle(GeometricShape):
    def __init__(self, length, width):
        """
        Initialize a rectangle with length and width.
        """
        self.length = length
        self.width = width

    def calculate_area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.length * self.width

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

class Circle(GeometricShape):
    def __init__(self, radius):
        """
        Initialize a circle with a radius.
        """
        self.radius = radius

    def calculate_area(self):
        """
        Calculate the area of the circle.
        """
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        """
        return 2 * math.pi * self.radius

class Triangle(GeometricShape):
    def __init__(self, side1, side2, side3):
        """
        Initialize a triangle with three side lengths.
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        """
        Calculate the area of the triangle using Heron's formula.
        """
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the triangle.
        """
        return self.side1 + self.side2 + self.side3

# Creating instances of different geometric shapes
rectangle = Rectangle(length=4, width=5)
circle = Circle(radius=3)
triangle = Triangle(side1=3, side2=4, side3=5)

# Testing the methods
print("Rectangle - Area:", rectangle.calculate_area(), "Perimeter:", rectangle.calculate_perimeter())
print("Circle - Area:", circle.calculate_area(), "Perimeter:", circle.calculate_perimeter())
print("Triangle - Area:", triangle.calculate_area(), "Perimeter:", triangle.calculate_perimeter())

# In this code:

# The GeometricShape class is a base class with methods for calculating area and perimeter. The methods are marked as abstract by raising NotImplementedError to enforce implementation in subclasses.
# Subclasses (Rectangle, Circle, Triangle) inherit from GeometricShape and implement their specific properties.
# Instances of different geometric shapes are created and their area and perimeter are calculated and printed.



