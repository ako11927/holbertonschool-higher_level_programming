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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Cast floats to integers
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    return a + b
