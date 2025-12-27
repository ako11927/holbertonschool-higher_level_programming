#!/usr/bin/python3
"""
This module provides functionality to convert CSV files to JSON format.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to JSON format and save it as data.json.
    
    Args:
        csv_filename (str): The name of the CSV file to convert
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csvfile:
            csv_data = list(csv.DictReader(csvfile))
        
        with open("data.json", mode='w', encoding='utf-8') as jsonfile:
            json.dump(csv_data, jsonfile, indent=4)
        
        return True
        
    except (FileNotFoundError, Exception):
        return False
