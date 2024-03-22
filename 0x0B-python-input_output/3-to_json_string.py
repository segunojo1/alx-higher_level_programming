#!/usr/bin/python3
"""json"""
import json


def to_json_string(my_obj):
    """to json string"""
    jsonstring = json.dumps(my_obj)
    return jsonstring
