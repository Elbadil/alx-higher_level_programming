#!/usr/bin/python3
"""Unittest for Rectangle class attributes and methods"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import sys
import io


class Test_Rectangle_Init(unittest.TestCase):
    """Tests for Rectangle's init"""

    def test_rectangle_parent(self):
        """check rectangle's parent class"""
        rect_1 = Rectangle(1, 4, 3, 2, 1)
        self.assertIsInstance(rect_1, Base)

    def test_rectangle_no_args(self):
        """Initialize a rectangle with no args"""
        with self.assertRaises(TypeError):
            rect_2 = Rectangle()

    def test_rectangle_one_arg(self):
        """Initialize a rectangle with one arg"""
        with self.assertRaises(TypeError):
            rect_3 = Rectangle(2)

    def test_rectangle_two_args(self):
        """Initialize a rectangle with two args"""
        width = 2
        height = 9
        rect_4 = Rectangle(width, height)
        self.assertEqual(rect_4.width, width)
        self.assertEqual(rect_4.height, height)

    def test_rectangle_three_args(self):
        """Initialize a rectangle with three args"""
        width = 2
        height = 9
        x = 3
        rect_5 = Rectangle(width, height, x)
        self.assertEqual(rect_5.width, width)
        self.assertEqual(rect_5.height, height)
        self.assertEqual(rect_5.x, x)

    def test_rectangle_four_args(self):
        """Initialize a rectangle with four args"""
        width = 2
        height = 9
        x = 3
        y = 1
        rect_6 = Rectangle(width, height, x, y)
        self.assertEqual(rect_6.width, width)
        self.assertEqual(rect_6.height, height)
        self.assertEqual(rect_6.x, x)
        self.assertEqual(rect_6.y, y)

    def test_rectangle_five_args(self):
        """Initialize a rectangle with five args"""
        width = 2
        height = 9
        x = 3
        y = 1
        rect_id = 2
        rect_7 = Rectangle(width, height, x, y, rect_id)
        self.assertEqual(rect_7.width, width)
        self.assertEqual(rect_7.height, height)
        self.assertEqual(rect_7.x, x)
        self.assertEqual(rect_7.y, y)
        self.assertEqual(rect_7.id, rect_id)

    def test_rectangle_six_args(self):
        """Initialize a rectangle with six args"""
        with self.assertRaises(TypeError):
            rect_8 = Rectangle(10, 12, 4, 8, 4, 8)


class Test_Rectangle_Width(unittest.TestCase):
    """Tests for Rectangle's width parameter"""

    def test_width_is_private(self):
        """width attribute is a private attribute"""
        rect = Rectangle(9, 8)
        with self.assertRaises(AttributeError):
            print(rect.__width)

    def test_integer_type_width(self):
        """Initialize Rectangle's width with integer as type"""
        width = 7
        height = 8
        rect_1 = Rectangle(width, height)
        self.assertEqual(rect_1.width, width)

    def test_non_integer_type_width(self):
        """Initialize Rectangle's width with non integer as type"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_2 = Rectangle("Three", 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_3 = Rectangle(7.8, 10)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect_4 = Rectangle({7, 8}, 10)

    def test_zero_value_width(self):
        """Initialize Rectangle's width with 0 as value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_5 = Rectangle(0, 10)

    def test_negative_value_width(self):
        """Initialize Rectangle's width with negative integer as value"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect_5 = Rectangle(-1, 10)


class Test_Rectangle_Height(unittest.TestCase):
    """Tests for Rectangle's width parameter"""

    def test_height_is_private(self):
        """Height attribute is a private attribute"""
        rect = Rectangle(9, 8)
        with self.assertRaises(AttributeError):
            print(rect.__height)

    def test_integer_type_height(self):
        """Initialize Rectangle's height with integer as type"""
        width = 7
        height = 8
        rect_1 = Rectangle(width, height)
        self.assertEqual(rect_1.height, height)

    def test_non_integer_type_height(self):
        """Initialize Rectangle's height with non integer as type"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_2 = Rectangle(7, "Ten")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_3 = Rectangle(7, 10.7)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect_4 = Rectangle(7, {10, 9})

    def test_zero_value_height(self):
        """Initialize Rectangle's height with 0 as value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_5 = Rectangle(10, 0)

    def test_negative_value_height(self):
        """Initialize Rectangle's height with 0 as value"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect_5 = Rectangle(10, -2)


class Test_Rectangle_x(unittest.TestCase):
    """Tests for Rectangle's x parameter"""

    def test_x_is_private(self):
        """x attribute is a private attribute"""
        rect = Rectangle(9, 8, 7)
        with self.assertRaises(AttributeError):
            print(rect.__x)

    def test_x_is_optional(self):
        """Initialize a new Rectangle without providing x"""
        width = 7
        height = 8
        rect_1 = Rectangle(width, height)
        self.assertEqual(rect_1.height, height)
        self.assertEqual(rect_1.width, width)

    def test_integer_type_x(self):
        """Initialize Rectangle's x with integer as type"""
        width = 7
        height = 8
        x = 2
        rect_1 = Rectangle(width, height, x)
        self.assertEqual(rect_1.x, x)

    def test_non_integer_type_x(self):
        """Initialize Rectangle's x with non integer as type"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_2 = Rectangle(7, 8, "Two")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_3 = Rectangle(7, 10, 8.2)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect_4 = Rectangle(7, 10, {9, 2})

    def test_zero_value_x(self):
        """Initialize Rectangle's x with 0 as value"""
        width = 7
        height = 8
        x = 0
        rect_1 = Rectangle(width, height, x)
        self.assertEqual(rect_1.x, x)

    def test_negative_value_x(self):
        """Initialize Rectangle's x with negative integer as value"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect_5 = Rectangle(10, 2, -1)


class Test_Rectangle_y(unittest.TestCase):
    """Tests for Rectangle's y parameter"""

    def test_y_is_private(self):
        """y attribute is a private attribute"""
        rect = Rectangle(9, 8, 7, 9)
        with self.assertRaises(AttributeError):
            print(rect.__y)

    def test_y_is_optional(self):
        """Initialize a new Rectangle without providing y"""
        width = 7
        height = 8
        rect_1 = Rectangle(width, height)
        self.assertEqual(rect_1.height, height)
        self.assertEqual(rect_1.width, width)

    def test_integer_type_y(self):
        """Initialize Rectangle's y with integer as type"""
        width = 7
        height = 8
        x = 2
        y = 3
        rect_1 = Rectangle(width, height, x, y)
        self.assertEqual(rect_1.y, y)

    def test_non_integer_type_y(self):
        """Initialize Rectangle's y with non integer as type"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_2 = Rectangle(7, 8, 1, "Five")

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_3 = Rectangle(7, 10, 8, 9.7)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect_4 = Rectangle(7, 10, 3, [2, 8])

    def test_zero_value_y(self):
        """Initialize Rectangle's y with 0 as value"""
        width = 7
        height = 8
        x = 2
        y = 0
        rect_1 = Rectangle(width, height, x, y)
        self.assertEqual(rect_1.y, y)

    def test_negative_value_y(self):
        """Initialize Rectangle's y with negative integer as value"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect_5 = Rectangle(10, 2, 1, -3)


class Test_Rectangle_Area(unittest.TestCase):
    """tests for Rectangle's area method"""

    def test_area_Rectangle_method(self):
        """test Rectangle's area method"""
        rect_1 = Rectangle(8, 9)
        self.assertEqual(rect_1.area(), 72)


class Test_Rectangle_Display(unittest.TestCase):
    """tests for Rectangle's display method"""

    def test_display_height_width(self):
        """tests for Rectangle's display method with only
        height and width.
        """
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with io.StringIO() as buffer:
            sys.stdout = buffer
            r.display()
            output = buffer.getvalue()
        self.assertEqual(expected_output, output)

    def test_display_all_args(self):
        """tests for Rectangle's display method with all args."""
        r = Rectangle(2, 3, 2, 3)
        expected_output = "\n\n\n  ##\n  ##\n  ##\n"
        with io.StringIO() as buffer:
            sys.stdout = buffer
            r.display()
            output = buffer.getvalue()
        self.assertEqual(expected_output, output)


class Test_Rectangle_str_method(unittest.TestCase):
    """tests for Rectangle's str method"""

    def test_str_rectangle_all_args(self):
        """test for str representation of a rectangle"""
        rect_1 = Rectangle(2, 5, 2, 4, 9)
        self.assertEqual(str(rect_1), "[Rectangle] (9) 2/4 - 2/5")

    def test_str_rectangle_width_height(self):
        """test for str representation of a rectangle with only height,
        width and id.
        """
        rect_2 = Rectangle(2, 5, 0, 0, 12)
        self.assertEqual(str(rect_2), "[Rectangle] (12) 0/0 - 2/5")


class Test_Rectangle_Update_Args(unittest.TestCase):
    """tests for Rectangle's update args method"""

    def setUp(self):
        """set up a new Rectangle"""
        self.rect = Rectangle(9, 8, 5, 7, 10)

    def test_update_one_arg(self):
        """test Rectangle's update args with one arg"""
        self.rect.update(7)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 5/7 - 9/8")

    def test_update_two_args(self):
        """test Rectangle's update args with two args"""
        self.rect.update(7, 11)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 5/7 - 11/8")

    def test_update_three_args(self):
        """test Rectangle's update args with two args"""
        self.rect.update(7, 11, 18)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 5/7 - 11/18")

    def test_update_four_args(self):
        """test Rectangle's update args with four args"""
        self.rect.update(7, 11, 18, 3)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 3/7 - 11/18")

    def test_update_five_args(self):
        """test Rectangle's update args with five args"""
        self.rect.update(7, 11, 18, 3, 2)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 3/2 - 11/18")

    def test_update_six_args(self):
        """test Rectangle's update args with six args"""
        self.rect.update(7, 11, 18, 3, 2, 19)
        self.assertEqual(str(self.rect), "[Rectangle] (7) 3/2 - 11/18")


class Test_Rectangle_Update_Kwargs(unittest.TestCase):
    """tests for Rectangle's update kwargs method"""

    def setUp(self):
        """set up a new Rectangle"""
        self.rect = Rectangle(16, 6, 7, 2, 13)

    def test_update_one_kwarg(self):
        """test Rectangle's update kwargs with one kwarg"""
        self.rect.update(id=11)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 7/2 - 16/6")

    def test_update_two_kwargs(self):
        """test Rectangle's update kwargs with two kwargs"""
        self.rect.update(id=11, x=1)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 1/2 - 16/6")

    def test_update_three_kwargs(self):
        """test Rectangle's update kwargs with three kwargs"""
        self.rect.update(id=11, x=1, width=6)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 1/2 - 6/6")

    def test_update_four_kwargs(self):
        """test Rectangle's update kwargs with four kwargs"""
        self.rect.update(id=11, x=1, width=6, height=9)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 1/2 - 6/9")

    def test_update_five_kwargs(self):
        """test Rectangle's update kwargs with five kwargs"""
        self.rect.update(id=11, x=1, width=6, height=9, y=4)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 1/4 - 6/9")

    def test_update_five_kwargs(self):
        """test Rectangle's update kwargs with five kwargs"""
        self.rect.update(id=11, x=1, width=6, height=9, y=4, u=7)
        self.assertEqual(str(self.rect), "[Rectangle] (11) 1/4 - 6/9")


class Test_Rectangle_Update_Args_Kwargs(unittest.TestCase):
    """tests for Rectangle's update args and kwargs method"""

    def test_update_args_kwargs(self):
        """test Rectangle's update args and kwags"""
        rect = Rectangle(8, 7, 2, 3, 11)
        rect.update(18, 2, 9, x=6, y=4)
        self.assertEqual(str(rect), "[Rectangle] (18) 2/3 - 2/9")


class Test_Rectangle_Dictionary(unittest.TestCase):
    """tests for Rectangle's dictionnary method"""

    def test_rectangle_dict(self):
        """tests for Rectangle's dictionnary method"""
        rect = Rectangle(8, 7, 2, 3, 11)
        rect_dict = rect.to_dictionary()
        self.assertEqual(str(rect_dict),
                         "{'x': 2, 'y': 3, 'id': 11, 'height': 7,"
                         " 'width': 8}")


if __name__ == "__main__":
    unittest.main()
