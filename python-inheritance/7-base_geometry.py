#!/usr/bin/python3
"""BaseGeometry class with integer validator"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Area method - not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if value is positive integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
