def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: An integer or float.
    - b: An integer or float (default is 98).

    Returns:
    An integer: the addition of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)

