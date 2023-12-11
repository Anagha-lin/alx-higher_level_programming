#!/usr/bin/python3
"""Base module"""

import json

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

if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)

