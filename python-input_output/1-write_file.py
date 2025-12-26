#!/usr/bin/python3
"""Module with write_file function"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
    and returns the number of chars
    """
    with open(filename, "w", encoding="UTF-8") as file:
        num = file.write(text)
        return num
