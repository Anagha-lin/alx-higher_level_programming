#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor method for Rectangle"""

        # Call the constructor of the Base class with the provided id
        super().__init__(id)

        # Validate and assign width using the setter
        self.width = width
        # Validate and assign height using the setter
        self.height = height
        # Validate and assign x using the setter
        self.x = x
        # Validate and assign y using the setter
        self.y = y

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

