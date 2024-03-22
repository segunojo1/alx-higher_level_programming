#!/usr/bin/python3
"""module for python io"""
import json


def save_to_json_file(my_obj, filename):
    """save json to file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
