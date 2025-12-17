#!/usr/bin/python3
"""Module for lookup function."""


def lookup(obj):
    """Return list of available attributes and methods of an object.

    Args:
        obj: Any object to get attributes and methods from.

    Returns:
        list: List of attribute and method names.
    """
    return dir(obj)
