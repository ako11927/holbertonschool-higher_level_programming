#!/usr/bin/python3
"""Module with Student class"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student
        If attrs is a list, only attributes in attrs are returned
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if attr in self.__dict__:
                    result[attr] = self.__dict__[attr]
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        from a dictionary
        """
        for key, value in json.items():
            setattr(self, key, value)
