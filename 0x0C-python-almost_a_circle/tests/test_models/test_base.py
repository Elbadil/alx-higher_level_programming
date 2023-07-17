#!/usr/bin/python3
"""Unittest for Base class attributes and methods"""
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class Test_Base_Init(unittest.TestCase):
    """Tests for Base's init"""

    def test_subclass_rectangle(self):
        """check base's subclass rectangle"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_subclass_square(self):
        """check base's subclass square"""
        self.assertTrue(issubclass(Square, Base))

    def test_base_no_arg(self):
        """Initialize a base with no args"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_base_one_arg(self):
        """Initialize a base with one arg"""
        base_id = 2
        b = Base(base_id)
        self.assertEqual(b.id, base_id)

    def test_base_two_arg(self):
        """Initialize a base with two args"""
        with self.assertRaises(TypeError):
            s = Base(9, 3)


class Test_Base_to_json_string(unittest.TestCase):
    """Tests for Base's to_json_string method"""

    def test_to_json_string_rectangle(self):
        """test to_json_string method on a ractangle class"""
        r = Rectangle(10, 9, 2, 1, 17)
        r_dict = r.to_dictionary()
        json_dict = Base.to_json_string([r_dict])
        self.assertEqual(str, type(json_dict))

    def test_to_json_string_square(self):
        """test to_json_string method on a square class"""
        s = Square(10, 9, 2, 7)
        s_dict = s.to_dictionary()
        json_dict = Base.to_json_string([s_dict])
        self.assertEqual(str, type(json_dict))

    def test_to_json_string_none(self):
        """test to_json_string method on none"""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        """test to_json_string method on an empty list"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_no_args(self):
        """test to_json_string method with no args"""
        with self.assertRaises(TypeError):
            json = Base.to_json_string()

    def test_to_json_string_one_arg(self):
        """test to_json_string method with one args"""
        s = Square(19, 9, 2, 7)
        s_dict = s.to_dictionary()
        json_dict = Base.to_json_string([s_dict])
        self.assertEqual(str, type(json_dict))

    def test_to_json_string_two_args(self):
        """test to_json_string method with two args"""
        with self.assertRaises(TypeError):
            json = Base.to_json_string([], "list")


class Test_Base_save_to_file(unittest.TestCase):
    """Tests for Base's save_to_file method"""

    def test_save_to_file_rectangle(self):
        """test save_to_file method on a ractangle class"""
        rect = Rectangle(10, 9, 2, 1, 17)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as File:
            file_content = File.read()
            self.assertTrue(len(file_content) == 54)

    def test_save_to_file_square(self):
        """test save_to_file method on a square class"""
        s = Square(10, 9, 2, 12)
        Square.save_to_file([s])
        with open("Square.json", "r") as File:
            file_content = File.read()
            self.assertTrue(len(file_content) == 40)

    def test_save_to_file_None(self):
        """test save_to_file method with none as argument"""
        Square.save_to_file(None)
        with open("Square.json", "r") as File:
            file_content = File.read()
            self.assertEqual(file_content, "[]")

    def test_save_to_file_two_args(self):
        """test save_to_file method with two args"""
        with self.assertRaises(TypeError):
            Square.save_to_file([], "Five")


class Test_Base_from_json_string(unittest.TestCase):
    """Tests for Base's save_to_file method"""

    def test_from_json_string_one_rectangle(self):
        """test from_json_string method on one rectangle"""
        list_input = [{'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        """test from_json_string method on two rectangles"""
        list_input = [{'id': 89, 'width': 10, 'height': 4},
                      {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        """test from_json_string method on one square"""
        list_input = [{'id': 89, 'size': 10}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        """test from_json_string method on two squares"""
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 13}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_object_type(self):
        """test from_json_string method to compare object type"""
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 13}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(type(list_input), type(list_output))

    def test_from_json_string_none(self):
        """test from_json_string method with none as argument"""
        self.assertEqual(Square.from_json_string(None), [])

    def test_from_json_two_args(self):
        """test from_json_string method with two args"""
        with self.assertRaises(TypeError):
            Square.from_json_string(1, "Five")


class Test_Base_create(unittest.TestCase):
    """Tests for Base's create method"""

    def test_create_rectangle_output(self):
        """test create method on a rectangle"""
        r = Rectangle(5, 3, 1, 4, 3)
        r_dict = r.to_dictionary()
        new_r = Rectangle.create(**r_dict)
        self.assertEqual(str(new_r), str(r))

    def test_create_rectangle_not_equal(self):
        """test create method on a rectangle"""
        r = Rectangle(5, 3, 1, 4, 3)
        r_dict = r.to_dictionary()
        new_r = Rectangle.create(**r_dict)
        self.assertNotEqual(new_r, r)

    def test_create_square_output(self):
        """test create method on a square"""
        s = Square(5, 3, 1, 4)
        s_dict = s.to_dictionary()
        new_s = Square.create(**s_dict)
        self.assertEqual(str(new_s), str(s))

    def test_create_square_not_equal(self):
        """test create method on a sqaure"""
        s = Square(5, 3, 1, 4)
        s_dict = s.to_dictionary()
        new_s = Square.create(**s_dict)
        self.assertNotEqual(new_s, s)


class Test_Base_load_from_file(unittest.TestCase):
    """Tests for Base's load_from_file method"""

    def test_load_from_file_one_rectangle(self):
        """test load_from_file method on a rectangle"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([r1])
        rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(rectangles_output[0]))

    def test_load_from_file_two_rectangles(self):
        """test load_from_file method on two rectangles"""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(rectangles_output[1]))

    def test_load_from_file_one_square(self):
        """test load_from_file method on one square"""
        s1 = Square(10, 7, 2, 8)
        Square.save_to_file([s1])
        squares_output = Square.load_from_file()
        self.assertEqual(str(s1), str(squares_output[0]))

    def test_load_from_file_two_squares(self):
        """test load_from_file method on two squares"""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(11, 9)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        squares_output = Square.load_from_file()
        self.assertEqual(str(s2), str(squares_output[1]))

    def test_load_from_file_two_args(self):
        """test load_from_file_two method with two args"""
        with self.assertRaises(TypeError):
            Base.load_from_file([], 1)


if __name__ == "__main__":
    unittest.main()
