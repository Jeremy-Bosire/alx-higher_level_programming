#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        try:
            value % 1 == 0
        except TypeError:
            print("width must be an integer")
        try:
            value > 0
        except ValueError:
            print("width must be >= 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self):
        try:
            value % 1 == 0
        except TypeError:
            print("height must be an integer")
        try:
            value > 0
        except ValueError:
            print("height must be >= 0")

