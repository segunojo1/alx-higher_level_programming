#!/usr/bin/python3
"""from json string"""
from json import JSONDecoder


def from_json_string(my_str):
    """function for jsoon string
    Args:
    my_str: str to convert
    """
    return JSONDecoder.decode(my_str)
