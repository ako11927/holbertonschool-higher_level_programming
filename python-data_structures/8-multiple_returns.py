#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns length and first character of a string."""
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
