#!/usr/bin/python3
"""Module with read_file function"""


def read_file(filename=""):
    """function reads a text file,
    and prints it
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
