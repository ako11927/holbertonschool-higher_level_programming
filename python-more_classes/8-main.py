#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10)
print(Rectangle.bigger_or_equal(r1, r2))
