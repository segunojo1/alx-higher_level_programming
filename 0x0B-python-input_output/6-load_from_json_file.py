#!/usr/bin/python3
"""python modules"""
from json import JSONDecoder


def load_from_json_file(filename):
    """load from json file"""
    lines = []
    with open(filename, encoding='utf-8') as file:
        for line in file.readlines():
            lines.append(line)
    return JSONDecoder().decode(''.join(lines))
