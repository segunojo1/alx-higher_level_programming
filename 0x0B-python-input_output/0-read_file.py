#!/usr/bin/python3
"""Defines the read file function"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding="utf-8") as f:
        filedata = f.read()
        print(filedata, end="")
