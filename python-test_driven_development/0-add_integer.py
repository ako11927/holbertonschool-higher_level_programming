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
    
    # Check for NaN (NaN is not equal to itself)
    if isinstance(a, float) and a != a:
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and b != b:
        raise ValueError("cannot convert float NaN to integer")
    
    # Check for infinity
    if isinstance(a, float) and (a == float('inf') or a == float('-inf')):
        raise ValueError("cannot convert float infinity to integer")
    if isinstance(b, float) and (b == float('inf') or b == float('-inf')):
        raise ValueError("cannot convert float infinity to integer")
    
    # Convert to integers
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    return a + b
