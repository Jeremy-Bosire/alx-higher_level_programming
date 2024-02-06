#!/usr/bin/python3
"""Addition of 2 integers

This module conatins a function, add_integer, that adds 2 integers
"""


def add_integer(a, b=98):
    """This is a function that adds 2 integers

    Args:
        a (int): The first parameter
        b (int): The second paramter. It has a default value of 98

    Returns:
        The sum of the two parameters inputted

    Raises:
        TypeError: If both 'a' and 'b' are not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
