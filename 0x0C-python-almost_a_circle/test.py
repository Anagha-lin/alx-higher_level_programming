#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base, Rectangle, Square
import os
import json
import csv
import turtle

class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def setUp(self):
        """Set up for test cases"""
        Base._Base__nb_objects = 0  # Reset the object counter

    def tearDown(self):
        """Clean up after test cases"""
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass

        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_to_json_string(self):
        """Test to_json_string method"""
        list_dicts = [{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'example'}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(type(json_string), str)
        self.assertEqual(json_string, '[{"id": 1, "name": "test"}, {"id": 2, "name": "example"}]')

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}, {"x": 0, "width": 2, "id": 2, "height": 4, "y": 0}]')

    def test_from_json_string(self):
        """Test from_json_string method"""
        json_string = '[{"id": 1, "name": "test"}, {"id": 2, "name": "example"}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(type(list_dicts), list)
        self.assertEqual(list_dicts, [{'id': 1, 'name': 'test'}, {'id': 2, 'name': 'example'}])

    def test_create(self):
        """Test create method"""
        dummy_dict = {'id': 1, 'x': 2, 'y': 3, 'width': 4, 'height': 5}
        r = Rectangle.create(**dummy_dict)
        self.assertEqual(type(r), Rectangle)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 5)

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(5, 6, 7, 8)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(type(list_rectangles_output), list)
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertEqual(type(list_rectangles_output[0]), Rectangle)
        self.assertEqual(list_rectangles_output[0].id, 1)
        self.assertEqual(list_rectangles_output[0].x, 3)
        self.assertEqual(list_rectangles_output[0].y, 4)
        self.assertEqual(list_rectangles_output[1].width, 6)

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        s1 = Square(1, 2, 3)
        s2 = Square(4, 5, 6)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        filename = "Square.csv"
        self.assertTrue(os.path.exists(filename))
        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '1,2,3\n4,5,6\n')

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        s1 = Square(1, 2, 3)
        s2 = Square(4, 5, 6)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(type(list_squares_output), list)
        self.assertEqual(len(list_squares_output), 2)
        self.assertEqual(type(list_squares_output[0]), Square)
        self.assertEqual(list_squares_output[0].id, 1)
        self.assertEqual(list_squares_output[0].x, 2)
        self.assertEqual(list_squares_output[1].size, 4)

    def test_draw(self):
        """Test draw method"""
        list_rectangles = [Rectangle(1, 2, 3, 4), Rectangle(5, 6, 7, 8)]
        list_squares = [Square(1, 2, 3), Square(4, 5, 6)]

        with self.assertRaises(SystemExit):
            Base.draw(list_rectangles, list_squares)

if __name__ == '__main__':
    unittest.main()

