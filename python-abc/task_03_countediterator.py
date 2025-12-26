#!/usr/bin/python3
"""
Task 3: CountedIterator
"""


class CountedIterator:
    """Iterator that counts items fetched"""
    
    def __init__(self, some_iterable):
        """Initialize with iterable"""
        self.iterator = iter(some_iterable)
        self.counter = 0
    
    def __next__(self):
        """Get next item and increment counter"""
        item = next(self.iterator)  # This will raise StopIteration if empty
        self.counter += 1
        return item
    
    def __iter__(self):
        """Return self as iterator"""
        return self
    
    def get_count(self):
        """Return current count"""
        return self.counter
