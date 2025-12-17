#!/usr/bin/python3
"""Module for checking if object inherits from a class."""


def inherits_from(obj, a_class):
    """Check if object inherits from specified class (directly or indirectly).

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj inherits from a_class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
