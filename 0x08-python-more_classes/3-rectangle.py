#!/usr/bin/python3
"""
This module defines a Rectangle class
"""


class Rectangle:
    """
    This class defines the attributes of a rectangle

    Attributes:
        width: width of the rectangle
        height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Creates new instances of class rectangle

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter.

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property setter for width of rectangle

        Args:
            value (int): width of the rectangle.

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Height getter.

        Returns:
            int: the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property setter for height of rectangle

        Args:
            value (int): height of the rectangle.

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than Zero
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: perimeter.
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2*(self.height + self.width)

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = []
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                rectangle.append("#")
                j += 1
            rectangle.append("\n")
            i += 1

        rectangle.pop()

        return "".join(rectangle)
