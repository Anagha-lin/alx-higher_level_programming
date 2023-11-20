#!/usr/bin/python3

def raise_exception():
    # Raise a type exception
    raise TypeError("This is a custom type exception")

# Example usage:
if __name__ == "__main__":
    try:
        raise_exception()

    except TypeError as e:
        print("Caught an exception:", e)

