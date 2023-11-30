#!/usr/bin/python3
"""
the name project.
"""

def say_my_name(first_name, last_name=""):
    """
    Print a message introducing the provided names.

    Args:
        first_name (str): String representing the first name.
        last_name (str): String representing the last name (optional).

    Raises:
        TypeError: If either first_name or last_name is not a string.
    """
    # Check if the provided names are strings
    if not all(isinstance(name, str) for name in (first_name, last_name)):
        raise TypeError('Both first_name and last_name must be strings')

    # Print a message introducing the names
    full_name = f"My name is {first_name} {last_name}"
    # Print the full name without an extra space at the end
    print(full_name if last_name else first_name)

# Example usage:
# say_my_name("John", "Doe")
# say_my_name("Alice")

