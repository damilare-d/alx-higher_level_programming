#!/usr/bin/python3
"""
The ``lazy_matrix_mul`` module
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """function that multiplies 2 matrices
        by using the module numpy
    Args:
        m_a ([]): mat a
        m_b ([]): mat b
    Returns:
        product of m_a & m_b
    """
    
    m_a = np.array(m_a)
    m_b = np.array(m_b)
    
    return np.matmul(m_a, m_b)
