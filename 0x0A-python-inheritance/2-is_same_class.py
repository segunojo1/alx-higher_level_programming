#!/usr/bin/python3
""" clas tester """


def is_same_class(obj, a_class):
    """ function to test obj equality """
    if isinstance(obj, a_class):
        return True
    else:
        return False
