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


if __name__ == "__main__":

    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
