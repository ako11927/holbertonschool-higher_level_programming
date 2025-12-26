#!/usr/bin/python3
"""
Task 5: The Mystical Dragon - Mastering Mixins
"""


class SwimMixin:
    """Mixin class providing swimming capability"""
    
    def swim(self):
        """Print swimming message"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class providing flying capability"""
    
    def fly(self):
        """Print flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying capabilities"""
    
    def roar(self):
        """Dragon-specific method to roar"""
        print("The dragon roars!")
