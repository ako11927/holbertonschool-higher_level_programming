#!/usr/bin/env python3
"""Test what Check 7 might be looking for"""
import task_01_duck_typing

# Test 1: Check if shape_info has isinstance checks
import inspect
source = inspect.getsource(task_01_duck_typing.shape_info)
print("shape_info source code:")
print(source)
print("\nDoes it contain 'isinstance'?", "isinstance" in source)
print("Does it contain 'type('?", "type(" in source)
print("Does it contain 'Shape'?", "Shape" in source)

# Test 2: Check method signatures
print("\nMethod signatures:")
for name in ['area', 'perimeter']:
    method = getattr(task_01_duck_typing.Circle, name)
    sig = inspect.signature(method)
    print(f"Circle.{name}{sig}")
    
    method = getattr(task_01_duck_typing.Rectangle, name)
    sig = inspect.signature(method)
    print(f"Rectangle.{name}{sig}")

# Test 3: Check abstract methods CORRECTLY
print("\nAbstract methods in Shape:")
for name in task_01_duck_typing.Shape.__abstractmethods__:
    print(f"  {name}")
    
# Test 4: Check if Shape can be instantiated
print("\nCan Shape be instantiated?")
try:
    s = task_01_duck_typing.Shape()
    print("  ERROR: Should not be able to instantiate Shape")
except TypeError as e:
    print(f"  GOOD: Cannot instantiate - {e}")
