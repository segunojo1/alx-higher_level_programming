#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """ Area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates int value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
