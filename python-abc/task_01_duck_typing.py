#!/usr/bin/python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class"""
    
    @abstractmethod
    def area(self):
        """Area method"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Perimeter method"""
        pass


class Circle(Shape):
    """Circle class"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing"""
    # Pure duck typing - we try to call the methods
    # If they don't exist, Python will raise AttributeError naturally
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
