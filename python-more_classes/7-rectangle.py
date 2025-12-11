#!/usr/bin/python3
"""Defines a Rectangle class with configurable print symbol."""

class Rectangle:
    """Represents a rectangle.

    Attributes:
        print_symbol (any): Symbol used for string representation.
    """

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle using the print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        line = symbol * self.width
        return "\n".join([line for _ in range(self.height)])

    def __repr__(self):
        """Return a string that recreates the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
