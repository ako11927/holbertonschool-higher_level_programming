#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return area - must be implemented"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Return perimeter - must be implemented"""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        """Return area of circle"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Return perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """Return area of rectangle"""
        return self.width * self.height
    
    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter - pure duck typing"""
    # Absolutely no type checking - just call methods
    a = shape.area()
    p = shape.perimeter()
    print(f"Area: {a}")
    print(f"Perimeter: {p}")
