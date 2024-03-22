#!/usr/bin/python3
"""Defines the write file"""


def write_file(filename="", text=""):
    """write file"""
    filewrite = 1
    with open(filename, mode="w", encoding="utf-8") as f:
        filewrite = f.write(text)
    return filewrite
