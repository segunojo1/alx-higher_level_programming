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

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area():
        return self.__width * self.__height

    def __str__(self):
        str = ""
        return str

    def __repr__(self):
        print(f"[Rectangle] {self.__width}/{self.__height}")

class Square(Rectangle):
    def __init__(self, size):
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area():
        return self.__size ** 2
