#!/usr/bin/python3
"""Square module"""

from rectangle import Rectangle

class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Square"""

        # Call the constructor of the Rectangle class with the provided id, x, y, and size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)
    print(s1.area())
    s1.display()

    print("---")

    s2 = Square(2, 2)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

