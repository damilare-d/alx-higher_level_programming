#!/usr/bin/python3
"""
This is the "2-matrix_divided" module
"""

def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix
    Args:
        matrix list(list((int) || (float))): a list of list of integers or floats
        div (int || float): number to divide each element in the matrix
    Returns:
        a new matrix
    """
    
    if ((type(matrix) is not list) or (type(div) not in [int, float])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if False in [True if type(row) == list else False for row in matrix]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if False in [True if type(col) in [int, float] else False for row in matrix for col in row]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZerorDivisionError("division by zero")
    return list(map(lambda row: list(map(lambda col: round(col/div, 2), row)), matrix))
