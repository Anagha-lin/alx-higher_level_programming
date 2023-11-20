#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        # Iterate through the list and print each element
        for i in range(x):
            print(my_list[i], end="")
            count += 1

    except IndexError:
        # Handle the case when the index is out of range
        pass

    finally:
        # Print a newline after the elements
        print()

    return count

