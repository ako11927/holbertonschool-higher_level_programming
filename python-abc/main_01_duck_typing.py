#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

class TestDuck:
    def area(self):
        return 123
    def perimeter(self):
        return 456

td = TestDuck()
shape_info(td)
"
