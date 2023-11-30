def say_my_name(first_name, last_name=""):
    # Check if the provided names are strings
    if not all(isinstance(name, str) for name in (first_name, last_name)):
        raise TypeError('Both first_name and last_name must be strings')

    # Print a message introducing the names
    print(f"My name is {first_name} {last_name}".strip())

