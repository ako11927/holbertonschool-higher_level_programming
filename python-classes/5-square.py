#!/usr/bin/python3
"""Module defining a Square class with print functionality."""


class Square:
    """Represents a square with print capability."""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using # characters."""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
