#!/usr/bin/python3
"""
Matrix multiplication module.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: Resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, or contains non-numeric elements.
        ValueError: If m_a or m_b is empty, not a rectangle, or cannot be multiplied.
    """
    # Matrix validation function
    def validate_matrix(matrix):
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or not matrix or any(not row for row in matrix):
            raise ValueError(f"{matrix} can't be empty or is not a list of lists")
        if any(not isinstance(element, (int, float)) for row in matrix for element in row):
            raise TypeError(f"{matrix} should contain only integers or floats")
        if any(len(row) != len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {matrix} must be of the same size")

    # Validate matrices
    validate_matrix(m_a)
    validate_matrix(m_b)

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication using list comprehension
    result_matrix = [[sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)] for row_a in m_a]

    return result_matrix


# Example usage:
# Uncomment the lines below to test the function with the provided matrices
# print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

