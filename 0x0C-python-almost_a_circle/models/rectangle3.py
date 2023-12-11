#!/usr/bin/python3
"""Rectangle module"""

from base import Base

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

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.validate_positive_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.validate_positive_integer("height", value)
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.validate_non_negative_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.validate_non_negative_integer("y", value)
        self.__y = value

    def validate_positive_integer(self, name, value):
        """Validate if the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_non_negative_integer(self, name, value):
        """Validate if the value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Calculate and return the area of the rectangle"""
        return self.__width * self.__height


if __name__ == "__main__":

    r1 = Rectangle(3, 2)
    print(r1.area())

    r2 = Rectangle(2, 10)
    print(r2.area())

    r3 = Rectangle(8, 7, 0, 0, 12)
    print(r3.area())
