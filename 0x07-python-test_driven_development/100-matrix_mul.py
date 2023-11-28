def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    for matrix, name in [(m_a, 'm_a'), (m_b, 'm_b')]:
        # Check if matrix is a list
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")

        # Check if matrix is a list of lists
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")

        # Check if matrix is not empty
        if not matrix or any(not row for row in matrix):
            raise ValueError(f"{name} can't be empty")

        # Check if elements are integers or floats
        if not all(isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError(f"{name} should contain only integers or floats")

        # Check if all rows have the same size
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {name} must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result_matrix = [
        [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
        for row_a in m_a
    ]

    return result_matrix
