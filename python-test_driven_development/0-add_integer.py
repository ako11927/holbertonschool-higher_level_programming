#!/usr/bin/python3
"""
This module defines the add_integer function.
It safely adds two numbers together, ensuring both are integers or floats.
Invalid float values such as NaN and infinity are also rejected to
maintain consistent behavior with integer casting.
"""


def add_integer(a, b=98):
    """
    Add two integers, converting floats to integers safely.

    Args:
        a: First value, must be int or float.
        b: Second value, must be int or float.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b is not a number or cannot be converted.
    """
    # Validate type for a
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Validate type for b
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and infinity BEFORE conversion
    if isinstance(a, float) and (a != a or a in (float('inf'), float('-inf'))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float('inf'), float('-inf'))):
        raise TypeError("b must be an integer")

    # Safe int conversion with error catching
    try:
        a = int(a)
    except Exception:
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except Exception:
        raise TypeError("b must be an integer")

    return a + b
