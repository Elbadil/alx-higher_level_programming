#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining unittest for the function max_integer(list=[])"""
    
    def test_sorted_list(self):
        """testing max_integer on a list with sorted numbers"""
        int_list = [20, 21, 22, 23]
        self.assertEqual(max_integer(int_list), 23)
    
    def test_non_sorted_list(self):
        """testing max_integer on a list with non-sorted numbers"""
        int_list = [102, 98, 3, 46]
        self.assertEqual(max_integer(int_list), 102)

    def test_negative_num_list(self):
        """testing max_integer on a list with negative numbers"""
        int_list = [-4, -20, -109, -2011]
        self.assertEqual(max_integer(int_list), -4)

    def test_empty_list(self):
        """testing max_integer on an empty list"""
        int_list = []
        self.assertEqual(max_integer(int_list), None)
    
    def test_mixed_num_list(self):
        """testing max_integer on a list eith mixed numbers
        of negative and positive numbers
        """
        int_list = [102, 98, -2, -200, 3, 46]
        self.assertEqual(max_integer(int_list), 102)

    def test_float_list(self):
        """testing max_integer on a list with floating_point numbers"""
        float_list = [15.8, 25.7, 2.8, 87.7]
        self.assertEqual(max_integer(float_list), 87.7)
    
    def test_duplicate_num_list(self):
        """testing max_integer on a list with duplicated numbers"""
        int_list = [2, 10, 2, 22, 10, 22]
        self.assertEqual(max_integer(int_list), 22)

    def test_range_num_list(self):
        """testing max_integer on a list with range of numbers"""
        int_list = list(range(2**4))
        self.assertEqual(max_integer(int_list), 15)
    
    def test_single_element_list(self):
        """testing max_integer on a list with a single element"""
        int_list = [55]
        self.assertEqual(max_integer(int_list), 55)
    
    def test_ints_floats_list(self):
        """testing max_integer on a list with a ints and floats"""
        int_float_list = [55, 66.7, 42, 2.4, 27]
        self.assertEqual(max_integer(int_float_list), 66.7)

    def test_str_list(self):
        """testing max_integer on a list of strings"""
        str_list = ["Hello", "there", "it's", "me"]
        self.assertEqual(max_integer(str_list), "there")

    def test_string(self):
        """testing max_integer on a string"""
        string = "Hello There"
        self.assertEqual(max_integer(string), "r")
    
    def test__empty_string(self):
        """testing max_integer on an empty string"""
        string = ""
        self.assertEqual(max_integer(string), None)


if __name__ == "__main__":
    unittest.main()
