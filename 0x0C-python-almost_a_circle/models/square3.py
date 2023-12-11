#!/usr/bin/python3
"""Square module"""

from rectangle import Rectangle

class Square(Rectangle):
    """Square class inheriting from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor method for Square"""

        # Call the constructor of the Rectangle class with the provided id, x, y, and size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square instance"""

        # If there are positional arguments, update attributes using *args
        if args:
            attributes = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])

        # Update attributes using **kwargs
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Override the __str__ method"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )




if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
