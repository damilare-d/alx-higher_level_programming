#!/usr/bin/python3
"""Module to test max_integer 
"""
import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """Method to test that max_integer returns None
            when an empty list is passed
        """
        self.assertEqual(max_integer([]), None)

    def test_max(self):
        """Method to test that max_integer returns an integer
        """
        self.assertEqual(max_integer([5, 7, 90]), 90)

    def test_str(self):
        """Method to test str in list
        """
        self.assertEqual(max_integer("Theophilus"), 'u')

    def test_negative(self):
        """Method to test negative integer
        """
        self.assertEqual(max_integer([-7, -6, -5, 0]), 0)

    def test_float(self):
        """Method to test float"""
        self.assertEqual(max_integer([1.71, 2.4, 0.5, 2.42]), 2.42)

    def test_int_float(self):
        """Method to test int and float in list"""
        self.assertEqual(max_integer([1.00, 1.01, 2, 4, 1.11]), 4)

    def test_duplicate(self):
        """Method to test duplicates"""
        self.assertEqual(max_integer([1, 9, 8, 9]), 9)

    def test_list_of_string(self):
        """Method to test list of strings"""
        self.assertEqual(max_integer(["Harry", "Van", "Ron"]), "Van")
    
    def test_error(self):
        """Method to test for TypeError"""
        with self.assertRaises(TypeError):
            max_integer(['Harry', 90, 9.1])

if __name__ == "__main__":
    unittest.main()
