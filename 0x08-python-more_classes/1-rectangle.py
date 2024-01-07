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
        self.__width = width
        self.__height = height

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

        Exceptions:
            TypeError: if width is not an integer
            ValueError: if width is less than zero
        """
        try:
            value % 1 == 0
            value > 0
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
        except Exception:
            pass

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

        Exceptions:
            TypeError: If height is not an integer
            ValueError: If height is less than Zero
        """
        try:
            value % 1 == 0
            value > 0
        except TypeError:
            print("height must be an integer")
        except ValueError:
            print("height must be >= 0")
        except Exception:
            pass
