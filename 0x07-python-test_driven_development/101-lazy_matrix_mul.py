import numpy as np

def lazy_matrix_mul(m_a, m_b):
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

    # Convert matrices to NumPy arrays and perform matrix multiplication
    result_matrix = np.dot(np.array(m_a), np.array(m_b))

    return result_matrix.tolist()
