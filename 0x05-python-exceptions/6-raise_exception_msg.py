#!/usr/bin/python3

def raise_exception_msg(message=""):
    # Raise a NameError with the specified message
    raise NameError(message)

# Example usage:
if __name__ == "__main__":
    try:
        raise_exception_msg("This is a custom name exception")

    except NameError as e:
        print("Caught an exception:", e)

