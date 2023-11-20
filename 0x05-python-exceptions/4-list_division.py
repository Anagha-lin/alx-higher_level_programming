#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                # Try to perform the division element-wise
                result = my_list_1[i] / my_list_2[i]

            except ZeroDivisionError:
                # Handle the case when the division is by zero
                result = 0
                print("division by 0")

            except (TypeError, ValueError):
                # Handle the case when an element is not an integer or float
                result = 0
                print("wrong type")

            except IndexError:
                # Handle the case when my_list_1 or my_list_2 is too short
                result = 0
                print("out of range")

            finally:
                # Append the result to the result_list
                result_list.append(result)

    finally:
        # Return the new list with all divisions
        return result_list

# Example usage:
if __name__ == "__main__":
    my_list_1 = [10, 20, 30]
    my_list_2 = [2, 5, 0]

    # Divide the lists with a list length of 4
    result = list_division(my_list_1, my_list_2, 4)
    print("Result:", result)

