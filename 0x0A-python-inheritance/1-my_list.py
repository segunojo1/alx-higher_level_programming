#!/usr/bin/python3
""" class to print list """


class MyList(list):
    """mylist class"""

    def __init__(self):
        """initialization of mylist"""
        super().__init__(self)

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
