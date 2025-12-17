#!/usr/bin/python3
"""Test all tasks."""
import sys

# Test Task 7
try:
    BaseGeometry = __import__('7-base_geometry').BaseGeometry
    bg = BaseGeometry()
    
    # Test 1: Wrong type
    try:
        bg.integer_validator("age", "hello")
        print("FAIL: Should raise TypeError")
    except TypeError as e:
        if str(e) == "age must be an integer":
            print("✓ Task 7: TypeError correct")
        else:
            print(f"FAIL: Wrong message: {e}")
    
    # Test 2: Zero
    try:
        bg.integer_validator("width", 0)
        print("FAIL: Should raise ValueError")
    except ValueError as e:
        if str(e) == "width must be greater than 0":
            print("✓ Task 7: ValueError correct")
        else:
            print(f"FAIL: Wrong message: {e}")
            
    # Test 3: Valid
    try:
        bg.integer_validator("height", 10)
        print("✓ Task 7: Valid input accepted")
    except:
        print("FAIL: Should accept valid input")
        
except Exception as e:
    print(f"Error importing Task 7: {e}")
