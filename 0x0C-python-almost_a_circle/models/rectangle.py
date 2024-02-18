#!/usr/bin/python3
"""Defines a Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle's position.
            y (int, optional): The y coordinate of the rectangle's position.
            id (int, optional): The identifier of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle's position."""
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle's position."""
        self.__y = value

