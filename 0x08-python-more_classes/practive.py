#!/usr/bin/python3

# Task 2
"""rectangle module"""

class Rectangle:
    """class of rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


#Task 3 4
#!/usr/bin/python3
"""rectangle class"""

class Rectangle:
    """a rectangle class instance"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """str"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += str(self.print_symbol)
            if i != self.__height - 1:
                str += "\n"
        return str

    def __repr__(self):
        """repr"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """when the object is deleted"""
        print("Bye rectangle...")
        if number_of_instances > 0:
            number_of_instances -= 1

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """get area"""
        return(self.__height * self.__width)
    
    def perimeter(self):
        """get perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return(2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2
