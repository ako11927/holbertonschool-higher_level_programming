#!/usr/bin/python3
"""
This module provides functions for JSON serialization and deserialization.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.
    
    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file
    """
    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.
    
    Args:
        filename: The filename of the input JSON file
        
    Returns:
        A Python Dictionary with the deserialized JSON data
    """
    with open(filename, "r") as file:
        return json.load(file)
