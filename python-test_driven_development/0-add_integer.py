#!/usr/bin/python3
"""
This module provides a function that adds two numbers together.
It ensures that both inputs are valid integers or floats before adding.
Float values are casted to integers after validating they are real numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers, casting floats to integers first.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        The integer result of a + b.

    Raises:
        TypeError: If a or b is not an integer or float,
        or if they are NaN or infinite values.
    """
    # Validate a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if isinstance(a, float) and (a != a or a in (float("inf"), float("-inf"))):
        raise TypeError("a must be an integer")

    # Validate b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(b, float) and (b != b or b in (float("inf"), float("-inf"))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
