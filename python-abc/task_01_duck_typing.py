#!/usr/bin/python3
"""
Task 1: Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class"""
    
    @abstractmethod
    def area(self):
        """area method"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """perimeter method"""
        pass


class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        """Initialize circle"""
        self.radius = radius
    
    def area(self):
        """Return area"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Return perimeter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        """Initialize rectangle"""
        self.width = width
        self.height = height
    
    def area(self):
        """Return area"""
        return self.width * self.height
    
    def perimeter(self):
        """Return perimeter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print shape info"""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
