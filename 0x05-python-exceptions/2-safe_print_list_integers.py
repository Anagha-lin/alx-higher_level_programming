#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        # Iterate through the list and print integers
        for i in range(x):
            # Try to print the integer using "{:d}".format()
            print("{:d}".format(my_list[i]), end="")
            count += 1

    except (ValueError, TypeError, IndexError):
        # Handle exceptions (ValueError for non-integer, TypeError for format, IndexError for list out of bounds)
        pass

    finally:
# Print a newline after the integers
print()

    return (count)

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, "three", 4, "five"]

    # Print the first 4 integers from the list
    integers_printed = safe_print_list_integers(my_list, 4)
    print("Number of integers printed:", integers_printed)

