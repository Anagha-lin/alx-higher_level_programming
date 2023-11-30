def say_my_name(first_name, last_name=""):
    # Check if the provided first name is a string
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    # Check if the provided last name is a string
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    # Print a message introducing the provided names
    print(f"My name is {first_name} {last_name}".strip())

