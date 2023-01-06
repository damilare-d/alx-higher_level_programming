#!/usr/bin/python3
"""
This is the "0-add-integer" module.

The 0-add-integer module supplies one function, add_integer()
"""

def add_integer(a, b=98):
    """Return the addition of a and b
    Args:
        a (int): first positional argument
        b (int): second positional argument with an optional value
    Returns:
        addition of a and b
    """

    if not a:
        raise TypeError
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)

