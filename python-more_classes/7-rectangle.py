#!/usr/bin/python3
"""Defines a Rectangle class with configurable print_symbol."""

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
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter (0 if width or height is 0)."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return the rectangle using the print_symbol.

        Uses the instance attribute if set, else falls back to the class
        attribute. The symbol is converted to string before repeating.
        """
        if self.width == 0 or self.height == 0:
            return ""
        # Prefer an instance-level symbol if present, otherwise the class-level one
        symbol = getattr(self, "print_symbol", type(self).print_symbol)
        symbol = str(symbol)
        line = symbol * self.width
        return "\n".join([line for _ in range(self.height)])

    def __repr__(self):
        """Return a string that recreates the rectangle."""
        return "Rectangle({}, {})".format(self.width, self.height)
