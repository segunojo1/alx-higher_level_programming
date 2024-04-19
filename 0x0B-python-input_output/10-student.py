#!/usr/bin/python3
"""module for student"""

class Student:
    """defines a student class"""
    def __init__(self, first_name, last_name, age):
        """instantiation with some values"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returs dicc rep of self"""
        return(self.__dict__)
