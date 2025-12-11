#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

r1 = Rectangle(2, 3)
r2 = Rectangle(4, 5)
print(Rectangle.number_of_instances)
del r1
print(Rectangle.number_of_instances)
