#!/usr/bin/env python3
"""Test true duck typing for Check 7"""
from task_01_duck_typing import shape_info

# Create a class that's NOT a Shape subclass
class MyDuck:
    def area(self):
        return 99
    
    def perimeter(self):
        return 66

# Create another duck-typed object
class Square:
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

print("Testing with MyDuck (not a Shape):")
my_duck = MyDuck()
shape_info(my_duck)

print("\nTesting with Square (not a Shape):")
square = Square(5)
shape_info(square)

print("\nTesting that shape_info doesn't check types:")
import inspect
source = inspect.getsource(shape_info)
if "isinstance" not in source and "type(" not in source:
    print("✓ shape_info uses pure duck typing")
else:
    print("✗ shape_info uses type checking")
