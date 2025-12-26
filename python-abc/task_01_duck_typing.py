#!/usr/bin/env python3
"""
Task 1: Shapes, Interfaces, and Duck Typing
Implement Shape abstract class and concrete Circle and Rectangle classes
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes with area and perimeter methods"""
    
    @abstractmethod
    def area(self):
        """Calculate area of the shape - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter of the shape - must be implemented by subclasses"""
        pass


class Circle(Shape):
    """Circle class implementing Shape interface"""
    
    def __init__(self, radius=0):
        """Initialize circle with radius"""
        self.radius = radius
    
    def area(self):
        """Calculate area of circle: π * r²"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate perimeter (circumference) of circle: 2 * π * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class implementing Shape interface"""
    
    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate area of rectangle: width * height"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate perimeter of rectangle: 2 * (width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing
    
    Args:
        shape: Object that has area() and perimeter() methods
    """
    # Using duck typing - we don't check type, just call the methods
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
