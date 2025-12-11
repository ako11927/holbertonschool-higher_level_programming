#!/usr/bin/python3
"""Defines a Rectangle class with configurable print_symbol."""


class Rectangle:
    """Represents a rectangle with a configurable printing symbol."""

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter or 0 if width or height is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Return rectangle drawn with `print_symbol`."""
        if self.width == 0 or self.height == 0:
            return ""
        # Use attribute lookup on the instance (instance attribute
        # overrides class attribute). Convert to string.
        symbol = str(self.print_symbol)
        line = symbol * self.width
        return "\n".join([line for _ in range(self.height)])

    def __repr__(self):
        """Return string that recreates the instance."""
        return "Rectangle({}, {})".format(self.width, self.height)

