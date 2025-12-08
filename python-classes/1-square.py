#!/usr/bin/python3
"""Module that defines a Square class with a private size."""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size):
        """Initialize the square.
        Args:
            size: size of the square (no validation).
        """
        self.__size = size
