#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        # Try to perform the division
        result = a / b

    except ZeroDivisionError:
        # Handle the case when b is 0 (division by zero)
        result = None

    except (TypeError, ValueError):
        # Handle the case when a or b is not an integer
        result = None

    finally:
        # Print the result in the finally section
        print("Inside result: {}".format(result))

    return result

# Example usage:
if __name__ == "__main__":
    # Test with valid division
    result = safe_print_division(10, 2)

    # Test with division by zero
    result = safe_print_division(5, 0)

    # Test with non-integer values
    result = safe_print_division("not", "an integer")

