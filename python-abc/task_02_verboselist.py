#!/usr/bin/env python3
"""Task 2: Extending the Python List with Notifications"""


class VerboseList(list):
    """A list that prints notifications for modifications"""
    
    def append(self, item):
        """Add an item to the end of the list and print notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend list by appending elements and print notification"""
        # Convert to list to get length if it's an iterator
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")
    
    def remove(self, item):
        """Remove first occurrence of item and print notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return item at index and print notification"""
        # Get the item before popping to print it
        item = self[index] if self else None
        result = super().pop(index)
        print(f"Popped [{result}] from the list.")
        return result
