#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

r = Rectangle(4, 2)
print(r)
Rectangle.print_symbol = "*"
print("After changing class print_symbol:")
print(r)

r.print_symbol = "$"
print("After changing instance print_symbol:")
print(r)
