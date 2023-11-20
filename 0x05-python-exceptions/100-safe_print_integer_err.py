#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        # Try to print the integer using "{:d}".format()
        print("{:d}".format(value))
        return True

    except (ValueError, TypeError) as e:
        # Handle the case when the value is not an integer
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return False

# Example usage:
if __name__ == "__main__":
    # Test with an integer
    result = safe_print_integer_err(42)
    print("Result:", result)

    # Test with a non-integer value
    result = safe_print_integer_err("Not an integer")
    print("Result:", result)

