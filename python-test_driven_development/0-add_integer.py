#!/usr/bin/python3
"""
This module provides the add_integer function.
It safely adds two numbers, ensuring they are valid integers or floats.
"""


def add_integer(a, b=98):
    """
    Add two numbers as integers.

    Args:
        a: first number (int or float)
        b: second number (int or float)

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b is not a number or cannot be converted to int
    """

    # Type check a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Type check b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN or Infinity for a
    if isinstance(a, float):
        if a != a or a in (float('inf'), float('-inf')):
            raise TypeError("a must be an integer")

    # Reject NaN or Infinity for b
    if isinstance(b, float):
        if b != b or b in (float('inf'), float('-inf')):
            raise TypeError("b must be an integer")

    # Safe conversion with error catching (OVERFLOW included)
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
