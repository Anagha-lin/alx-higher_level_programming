def replace_in_list(my_list, idx, element):
    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return my_list  # Return the original list without modification
    
    # Replace the element at the specified index
    my_list[idx] = element
    
    return my_list
