#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info, Shape

# Test 1: Basic functionality
print("Test 1: Basic shapes")
circle = Circle(5)
rectangle = Rectangle(4, 7)

shape_info(circle)
shape_info(rectangle)

# Test 2: Verify abstract class
print("\nTest 2: Abstract class check")
try:
    shape = Shape()
    print("FAIL: Should not instantiate Shape")
except TypeError as e:
    print(f"PASS: Cannot instantiate Shape - {e}")

# Test 3: Verify duck typing
print("\nTest 3: Duck typing verification")

class NotAShape:
    def area(self):
        return 100
    def perimeter(self):
        return 50

not_a_shape = NotAShape()
shape_info(not_a_shape)
