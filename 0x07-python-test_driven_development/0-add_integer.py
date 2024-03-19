#!/usr/bin/python3
def add_integer(a, b=98):
    """add integer adds to two integers
    Args:
        a: first number to be added
        b: second number to be added
    Return:
        returns the sum of the integers
    """
    if (not (isinstance(a, int)) and not (isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not (isinstance(b, int)) and not (isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
