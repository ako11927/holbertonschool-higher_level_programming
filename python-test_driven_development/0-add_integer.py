#!/usr/bin/python3
"""Module for add_integer function."""


def add_integer(a, b=98):
    """Add two integers.
    Args:
        a: First number, must be integer or float
        b: Second number, must be integer or float, defaults to 98
    Returns:
        The sum of a and b as an integer
    Raises:
        TypeError: If a or b is not an integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except OverflowError:
        raise ValueError("cannot convert float infinity to integer")
