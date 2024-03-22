#!/usr/bin/python3
"""Defines the write file"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
        return len(text)
