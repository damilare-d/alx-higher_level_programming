#!/usr/bin/python3

"""Define a class LockedClass"""


class LockedClass:
    """
    A representation of LockedClass
    with no class or object attribute, that
    prevents the user from dynamically creating
    new instance atrributes except if the new
    instance attribute is called first_name
    """ 
    __slots__ = ["first_name"]
