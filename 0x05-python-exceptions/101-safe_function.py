#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        # Try to execute the function with the provided arguments
        result = fct(*args)
        return result

    except Exception as e:
        # Handle any exception that might occur during the function execution
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return None

# Example usage:
if __name__ == "__main__":
    # Define a sample function that might raise an exception
    def sample_function(x, y):
        return x / y

    # Test the safe_function with the sample function
    result = safe_function(sample_function, 10, 2)
    print("Result:", result)

    # Test with a function that might raise an exception
    result = safe_function(sample_function, 10, 0)
    print("Result:", result)

