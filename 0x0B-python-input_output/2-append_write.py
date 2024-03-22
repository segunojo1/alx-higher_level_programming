#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """appends"""
    n = 0
    with open(filename, mode="a", encoding="utf-8") as f:
        n = f.write(text)
    return n
    