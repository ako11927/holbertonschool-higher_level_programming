#!/usr/bin/python3
"""This module defines Shape abstract class and concrete implementations."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract class representing a shape."""

    @abstractmethod
    def area(self):
        """Abstract method to calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to calculate perimeter."""
        pass


class Circle(Shape):
    """A class representing a circle."""

    def __init__(self, radius):
        """Initialize the circle with a radius.

        Args:
            radius: The radius of the circle.
        """
        self.radius = abs(radius)

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            The area of the circle (pi * radius^2).
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter of the circle.

        Returns:
            The perimeter of the circle (2 * pi * radius).
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle.

        Returns:
            The area of the rectangle (width * height).
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle (2 * (width + height)).
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape using duck typing.

    Args:
        shape: An object with area and perimeter methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
