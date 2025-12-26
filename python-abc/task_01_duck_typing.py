#!/usr/bin/python3
"""Task 1: Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape"""
        pass


class Circle(Shape):
    """Circle class that inherits from Shape"""
    
    def __init__(self, radius):
        """Initialize a circle with given radius"""
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""
    
    def __init__(self, width, height):
        """Initialize a rectangle with given width and height"""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Write a standalone function named shape_info that accepts an object of type Shape
    (by duck typing) and prints its area and perimeter.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
