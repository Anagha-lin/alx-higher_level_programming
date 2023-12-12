import os
import unittest
from base import Base
from rectangle import Rectangle
from square import Square


class TestBaseInstantiation(unittest.TestCase):
    def test_default_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_multiple_instances_id_increment(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_none_id_default_increment(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    # Additional test cases for various ID types...

    def test_two_args_raises_error(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJsonString(unittest.TestCase):
    def test_rectangle_json_string_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    # ... (rephrased other test cases for to_json_string)


class TestBaseSaveToFile(unittest.TestCase):
    def tearDown(self):
        # Delete any created files
        for filename in ["Rectangle.json", "Square.json", "Base.json"]:
            try:
                os.remove(filename)
            except IOError:
                pass

    # ... (rephrased other test cases for save_to_file)


# ... (rephrased other test classes)

if __name__ == "__main__":
    unittest.main()

