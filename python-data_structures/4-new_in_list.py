#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces element at index in a copy of list."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy
    new_list = my_list[:]  # Create a copy
    new_list[idx] = element
    return new_list

