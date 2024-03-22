#!/usr/bin/python3

"""returns True if the object is exactly an instance of the specified class"""
def is_same_class(obj, a_class):
    if isinstance(obj, a_class):
        return True
    else:
        return False


class BaseGeometry:
    """geometry"""
    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates int value"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        else:
            if value <= 0:
                raise ValueError("<name> must be greater than 0")