#!/usr/bin/python3
"""
Task 4: The Enigmatic FlyingFish - Exploring Multiple Inheritance
"""


class Fish:
    """Fish class with swimming and habitat behaviors"""
    
    def swim(self):
        """Print fish swimming message"""
        print("The fish is swimming")
    
    def habitat(self):
        """Print fish habitat message"""
        print("The fish lives in water")


class Bird:
    """Bird class with flying and habitat behaviors"""
    
    def fly(self):
        """Print bird flying message"""
        print("The bird is flying")
    
    def habitat(self):
        """Print bird habitat message"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""
    
    def fly(self):
        """Override Bird's fly method for flying fish"""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override Fish's swim method for flying fish"""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override habitat method for flying fish"""
        print("The flying fish lives both in water and the sky!")
