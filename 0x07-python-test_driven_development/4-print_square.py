#!/usr/bin/python3
"""
The `4-print_square` module file
"""

def print_square(size):
    """Function that prints a square with the character #.
    Args:
        size (int): length of the square
    Returns:
        character `#*size`
    """


    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    i = 0
    while i < size:
        print("{}".format("#"*size), end="\n")
        i += 1

