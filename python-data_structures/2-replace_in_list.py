#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element of a list at a specific position.
    
    Args:
        my_list: The list to modify
        idx: The index at which to replace the element
        element: The new element to insert
    
    Returns:
        The modified list if idx is valid, otherwise the original list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    
    my_list[idx] = element
    return my_list
