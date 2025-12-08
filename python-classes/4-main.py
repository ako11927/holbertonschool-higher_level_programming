#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print(my_square.size)
print(my_square.area())

my_square.size = 3
print(my_square.size)
print(my_square.area())

try:
    my_square.size = "5 feet"
    print(my_square.size)
except Exception as e:
    print(e)
