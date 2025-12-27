#!/usr/bin/python3
"""
This module provides a CustomObject class with pickle serialization capabilities.
"""
import pickle


class CustomObject:
    """
    A custom class that can be serialized and deserialized using pickle.

    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize a CustomObject with name, age, and student status."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes in a formatted way."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): The filename to save the serialized object
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename (str): The filename to load the serialized object from

        Returns:
            CustomObject: The deserialized object, or None if an error occurs
        """
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.UnpicklingError, Exception):
            return None
