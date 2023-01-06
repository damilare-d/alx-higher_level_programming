#!/usr/bin/python3
"""
The ``100-matrix_mul`` module file
"""

def matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices.
    Args:
        m_a ([[]]): first matrix
        m_b ([[]]): second matrix
    Returns:
        a new matrix
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    m = len(m_a)
    n = len(m_a[0])
    p = len(m_b)
    q = len(m_b[0])
    row, col, i, j, k = 0, 0, 0, 0, 0
    m_c = [[0 for col in range(q)] for row in range(m)]

    for i in range(0, m):
        for j in range(0, q):
            for k in range(0, p):
                m_c[i][j] += m_a[i][k] * m_b[k][j]

    return m_c
