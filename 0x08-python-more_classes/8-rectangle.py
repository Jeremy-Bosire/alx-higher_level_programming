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
        number_of_instances: number of instances created
        print_symbol: # symbol
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Creates new instances of class rectangle

        Args:
            width (int, optional): width of rectangle. Defaults to 0.
            height (int, optional): height of rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """
        Prints the rectangle with the character #

        Returns:
            str: the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = []
        i = 0
        while i < self.height:
            j = 0
            while j < self.width:
                rectangle.append(str(self.print_symbol))
                j += 1
            rectangle.append("\n")
            i += 1
        # removes blank line
        rectangle.pop()

        return "".join(rectangle)

    def __repr__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: the rectangle representation
        """

        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of the Rectangle class is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the area of two rectangles and compares them.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Returns:
            Rectangle: the rectangle with the biggest area else rect_1 if
            areas are equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1

        return rect_2
