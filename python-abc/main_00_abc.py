#!/usr/bin/env python3
"""Test for task_00_abc.py"""
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

# This should raise TypeError as Animal is abstract
# animal = Animal()
# print(animal.sound())
