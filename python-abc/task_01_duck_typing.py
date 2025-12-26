#!/usr/bin/python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape abstract class"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        """Initialize with radius"""
        self.radius = radius
    
    def area(self):
        """Return area of circle"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Return perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        """Initialize with width and height"""
        self.width = width
        self.height = height
    
    def area(self):
        """Return area of rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing"""
    # Absolutely no type checking - pure duck typing
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
