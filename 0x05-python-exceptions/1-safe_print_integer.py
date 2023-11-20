#!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Try to print the integer using "{:d}".format()
        print("{:d}".format(value))

    except (ValueError, TypeError):
        # Handle the case when the value is not an integer
        return False

    else:
        # Return True if the value is an integer and printed correctly
        return True

# Example usage:
if __name__ == "__main__":
    # Test with an integer
    result = safe_print_integer(42)
    print("Result:", result)

    # Test with a non-integer value
    result = safe_print_integer("Not an integer")
    print("Result:", result)

