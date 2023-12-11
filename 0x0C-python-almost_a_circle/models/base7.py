#!/usr/bin/python3
"""Base module"""

import json
import csv
import turtle

class Base:
    """Base class for managing id attribute"""

    # Private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for Base"""

        # If id is not None, assign it to the public instance attribute id
        if id is not None:
            self.id = id
        # If id is None, increment __nb_objects and assign the new value to id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string"""

        # If the list is None or empty, return "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        # Otherwise, return the JSON string representation of the list of dictionaries
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of instances to a JSON file"""

        # If list_objs is None, save an empty list
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__
        # Create the filename
        filename = "{}.json".format(class_name)

        # Convert the list of instances to a list of dictionaries
        dict_list = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to a JSON string
        json_string = cls.to_json_string(dict_list)

        # Write the JSON string to the file
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries"""

        # If json_string is None or empty, return an empty list
        if json_string is None or len(json_string) == 0:
            return []

        # Otherwise, return the list represented by json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set"""

        # Create a dummy instance
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        # Update the dummy instance with the real values from the dictionary
        dummy_instance.update(**dictionary)

        # Return the created instance
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file"""

        # Get the class name
        class_name = cls.__name__
        # Create the filename
        filename = "{}.json".format(class_name)

        try:
            # Read the content of the file
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []

        # Convert the JSON string to a list of dictionaries
        dict_list = cls.from_json_string(json_string)

        # Create instances from the list of dictionaries
        instances = [cls.create(**d) for d in dict_list]

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of instances to a CSV file"""

        # If list_objs is None, save an empty list
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__
        # Create the filename
        filename = "{}.csv".format(class_name)

        # Open the CSV file for writing
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            # Iterate through the list of instances
            for obj in list_objs:
                # Get the values as a list
                values = [getattr(obj, attr) for attr in cls.get_attributes()]
                # Write the values to the CSV file
                writer.writerow(values)

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from a CSV file"""

        # Get the class name
        class_name = cls.__name__
        # Create the filename
        filename = "{}.csv".format(class_name)

        try:
            # Open the CSV file for reading
            with open(filename, "r") as file:
                reader = csv.reader(file)
                # Read the rows from the CSV file
                rows = [row for row in reader]
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            return []

        # Get the attribute names for the class
        attributes = cls.get_attributes()

        # Create instances from the rows in the CSV file
        instances = [cls.create(**dict(zip(attributes, map(cls.convert_to_int, row)))) for row in rows]

        return instances

    @classmethod
    def convert_to_int(cls, value):
        """Convert a string to an integer if possible"""

        try:
            return int(value)
        except ValueError:
            return value

    @classmethod
    def get_attributes(cls):
        """Get the attribute names for the class"""

        # Get the attributes from the class dictionary
        return [attr for attr in dir(cls) if not callable(getattr(cls, attr)) and not attr.startswith("__")]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using the Turtle graphics module"""

        turtle.title("Rectangles and Squares")

        # Draw rectangles
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.color("black")
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
            turtle.end_fill()

        # Draw squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            turtle.color("black")
            turtle.begin_fill()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)
            turtle.end_fill()

        turtle.exitonclick()


if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file_csv()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file_csv(list_squares_input)

    list_squares_output = Square.load_from_file_csv()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

    print("---")
    
    Base.draw(list_rectangles_output, list_squares_output)

