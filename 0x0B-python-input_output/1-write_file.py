#!/usr/bin/python3

def write_file(filename="", text=""):
    """write file"""
    with open(filename, encoding="utf-8") as f:
        fwrite = f.write(filename, text)
        return len(fwrite)