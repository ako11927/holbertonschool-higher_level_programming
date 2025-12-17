#!/usr/bin/python3
"""
Module for BaseGeometry class with integer validation.
"""


class BaseGeometry:
    """
    A base geometry class with area method and integer validation.
    """

    def area(self):
        """
        Calculate the area (not implemented).
        
        Raises:
            Exception: Always raises exception with message.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
