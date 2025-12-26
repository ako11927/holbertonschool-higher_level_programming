#!/usr/bin/python3
"""Module with append_write function"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file
     and returns the number of characters added
    """
    with open(filename, "a", encoding="UTF-8") as file:
        append_text = file.write(text)
        return append_text
