#!/usr/bin/python3

def write_file(filename="", text=""):
    """write file"""
    with open(filename, encoding="utf-8") as f:
        f.write(text)
        return len(text)