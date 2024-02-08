#!/usr/bin/python3
""""Defines an add integer func"""


def add_integer(a, b=98):
    """It returns an integer addition of a and b"""


    if((not isinstance (a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b)) 
