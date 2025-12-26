#!/usr/bin/env python3
"""Test the shapes implementation"""
from task_01_duck_typing import Circle, Rectangle, shape_info

# Test 1: Basic functionality
circle = Circle(5)
print("Circle with radius 5:")
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")

# Test 2: Rectangle
rect = Rectangle(4, 7)
print("\nRectangle 4x7:")
print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")

# Test 3: shape_info function
print("\nTesting shape_info function:")
shape_info(circle)
shape_info(rect)

# Test 4: Try to instantiate abstract class (should fail)
try:
    from task_01_duck_typing import Shape
    s = Shape()
except TypeError as e:
    print(f"\nCorrectly cannot instantiate Shape: {e}")
