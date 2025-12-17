#!/usr/bin/python3
"""Module for MyList class that inherits from list."""


class MyList(list):
    """A class that inherits from list with additional functionality."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
