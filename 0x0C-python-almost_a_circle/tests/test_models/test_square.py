#!/usr/bin/python3
"""Unittest for Square class attributes and methods"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square
import sys
import io


class Test_Square_Init(unittest.TestCase):
    """Tests for Square's init"""

    def test_square_parent(self):
        """check square's parent class"""
        s_1 = Square(1, 3, 2, 1)
        self.assertIsInstance(s_1, Rectangle)

    def test_square_grand_parent(self):
        """check rectangle's grand parent class"""
        s_1 = Square(1, 3, 2, 1)
        self.assertIsInstance(s_1, Base)

    def test_square_no_args(self):
        """Initialize a square with no args"""
        with self.assertRaises(TypeError):
            s_2 = Square()

    def test_square_one_arg(self):
        """Initialize a square with one arg"""
        size = 3
        s = Square(size)
        self.assertEqual(s.size, size)

    def test_square_two_args(self):
        """Initialize a square with two args"""
        size = 4
        x = 2
        s = Square(size, x)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)

    def test_square_three_args(self):
        """Initialize a square with three args"""
        size = 4
        x = 2
        y = 3
        s = Square(size, x, y)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)
        self.assertEqual(s.y, y)

    def test_square_four_args(self):
        """Initialize a square with four args"""
        size = 4
        x = 2
        y = 3
        s_id = 2
        s = Square(size, x, y, s_id)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)
        self.assertEqual(s.y, y)
        self.assertEqual(s.id, s_id)

    def test_square_five_args(self):
        """Initialize a square with five args"""
        with self.assertRaises(TypeError):
            s = Square(4, 5, 9, 10, 11)


class Test_Square_Size(unittest.TestCase):
    """Tests for Square's size parameter"""

    def test_integer_type_size(self):
        """Initialize Square's size with integer as type"""
        size = 8
        s = Square(size)
        self.assertEqual(s.size, size)

    def test_non_integer_type_size(self):
        """Initialize Square's size with non integer as type"""
        with self.assertRaises(TypeError):
            s = Square(8.5)

        with self.assertRaises(TypeError):
            s = Square("Eight")

        with self.assertRaises(TypeError):
            s = Square(True)

        with self.assertRaises(TypeError):
            s = Square((7, ))

    def test_zero_value_size(self):
        """Initialize Square's size with 0 as value"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_negative_value_size(self):
        """Initialize Square's size with negative integer as value"""
        with self.assertRaises(ValueError):
            s = Square(-5)


class Test_Square_x(unittest.TestCase):
    """Tests for Square's x parameter"""

    def test_x_is_optional(self):
        """Initialize a new Square without providing x"""
        size = 9
        s = Square(size)
        self.assertEqual(s.size, size)

    def test_integer_type_x(self):
        """Initialize Square's x with integer as type"""
        size = 10
        x = 2
        s = Square(size, x)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)

    def test_non_integer_type_x(self):
        """Initialize Square's x with non integer as type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(7, "Two")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(7, 8.2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(7, {9, 2})

    def test_zero_value_x(self):
        """Initialize Square's x with 0 as value"""
        size = 3
        x = 0
        s = Square(size, x)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)

    def test_negative_value_x(self):
        """Initialize Square's x with negative integer as value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(10, -1)


class Test_Square_y(unittest.TestCase):
    """Tests for Square's y parameter"""

    def test_y_is_optional(self):
        """Initialize a new Square without providing y"""
        size = 9
        s = Square(size)
        self.assertEqual(s.size, size)

    def test_integer_type_y(self):
        """Initialize Square's y with integer as type"""
        size = 10
        x = 2
        y = 3
        s = Square(size, x, y)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)
        self.assertEqual(s.y, y)

    def test_non_integer_type_y(self):
        """Initialize Square's y with non integer as type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(7, 8, "Five")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(7, 8, 10.6)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(7, 8, {9, 2})

    def test_zero_value_y(self):
        """Initialize Square's y with 0 as value"""
        size = 3
        x = 7
        y = 0
        s = Square(size, x, y)
        self.assertEqual(s.size, size)
        self.assertEqual(s.x, x)
        self.assertEqual(s.y, y)

    def test_negative_value_y(self):
        """Initialize Square's y with negative integer as value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(10, 3, -4)


class Test_Square_Area(unittest.TestCase):
    """tests for Square's area method"""

    def test_area_square_method(self):
        """test Square's area method"""
        s = Square(8)
        self.assertEqual(s.area(), 64)


class Test_Square_Display(unittest.TestCase):
    """tests for Square's display method"""

    def test_display_size(self):
        """tests for Square's display method with only size"""
        s = Square(2)
        expected_output = "##\n##\n"
        with io.StringIO() as buffer:
            sys.stdout = buffer
            s.display()
            output = buffer.getvalue()
        self.assertEqual(expected_output, output)

    def test_display_all_square_args(self):
        """tests for Square's display method with all args."""
        s = Square(2, 3, 2)
        expected_output = "\n\n   ##\n   ##\n"
        with io.StringIO() as buffer:
            sys.stdout = buffer
            s.display()
            output = buffer.getvalue()
        self.assertEqual(expected_output, output)


class Test_Square_str_method(unittest.TestCase):
    """tests for Square's str method"""

    def test_str_square_all_args(self):
        """test for str representation of a Square"""
        s = Square(2, 2, 4, 9)
        self.assertEqual(str(s), "[Square] (9) 2/4 - 2")

    def test_str_square_size(self):
        """test for str representation of a Square with only
        size and id.
        """
        s = Square(5, 0, 0, 19)
        self.assertEqual(str(s), "[Square] (19) 0/0 - 5")


class Test_Square_Update_Args(unittest.TestCase):
    """tests for Square's update Args method"""

    def setUp(self):
        """set up a new Square"""
        self.s = Square(16, 7, 2, 13)

    def test_update_one_arg(self):
        """test Square's update args with one arg"""
        self.s.update(7)
        self.assertEqual(str(self.s), "[Square] (7) 7/2 - 16")

    def test_update_two_arg(self):
        """test Square's update args with two args"""
        self.s.update(7, 5)
        self.assertEqual(str(self.s), "[Square] (7) 7/2 - 5")

    def test_update_three_arg(self):
        """test Square's update args with three args"""
        self.s.update(7, 5, 4)
        self.assertEqual(str(self.s), "[Square] (7) 4/2 - 5")

    def test_update_four_arg(self):
        """test Square's update args with four args"""
        self.s.update(7, 5, 4, 9)
        self.assertEqual(str(self.s), "[Square] (7) 4/9 - 5")

    def test_update_five_arg(self):
        """test Square's update args with five args"""
        self.s.update(7, 5, 4, 9, 2)
        self.assertEqual(str(self.s), "[Square] (7) 4/9 - 5")


class Test_Square_Update_Kwargs(unittest.TestCase):
    """tests for Square's update Args method"""

    def setUp(self):
        """set up a new Square"""
        self.s = Square(16, 7, 2, 13)

    def test_update_one_kwarg(self):
        """test Square's update args with one kwarg"""
        self.s.update(size=7)
        self.assertEqual(str(self.s), "[Square] (13) 7/2 - 7")

    def test_update_two_kwargs(self):
        """test Square's update args with two kwargs"""
        self.s.update(size=7, id=3)
        self.assertEqual(str(self.s), "[Square] (3) 7/2 - 7")

    def test_update_three_kwargs(self):
        """test Square's update args with three kwargs"""
        self.s.update(size=7, id=3, y=1)
        self.assertEqual(str(self.s), "[Square] (3) 7/1 - 7")

    def test_update_four_kwargs(self):
        """test Square's update args with four kwargs"""
        self.s.update(size=7, id=3, y=1, x=3)
        self.assertEqual(str(self.s), "[Square] (3) 3/1 - 7")

    def test_update_five_kwargs(self):
        """test Square's update args with five kwargs"""
        self.s.update(size=7, id=3, y=1, x=3, u=3)
        self.assertEqual(str(self.s), "[Square] (3) 3/1 - 7")


class Test_Square_Update_Args_Kwargs(unittest.TestCase):
    """tests for Square's update args and kwargs method"""

    def test_update_args_kwargs(self):
        """test Square's update args and kwags"""
        s = Square(8, 7, 3, 11)
        s.update(18, 2, x=6, y=4)
        self.assertEqual(str(s), "[Square] (18) 7/3 - 2")


class Test_Square_Dictionary(unittest.TestCase):
    """tests for Square's dictionnary method"""

    def test_Square_dict(self):
        """tests for Square's dictionnary method"""
        s = Square(8, 7, 3, 11)
        s_dict = s.to_dictionary()
        self.assertEqual(str(s_dict),
                         "{'id': 11, 'x': 7, 'size': 8, 'y': 3}")


if __name__ == "__main__":
    unittest.main()
