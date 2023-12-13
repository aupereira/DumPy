# Contains core linalg functions that return vectors.

type Vector = list[float or int]
type Matrix = list[Vector]

def outer(v1: Vector, v2: Vector) -> Vector:
    """Computes the outer product of two vectors.

    Args:
        v1 (list): The first vector.
        v2 (list): The second vector.

    Returns:
        Vector: The outer product matrix.

    Raises:
        ValueError: If the vectors are not of the same length.
    """

    l1 = len(v1)
    l2 = len(v2)

    if l1 != l2:
        raise ValueError("Vectors must be of same length.")

    out = [[None] * l1 for _ in range(l1)]

    for i in range(l1):
        for j in range(l1):
            out[i][j] = v1[i] * v2[j]

    return out

def mvmul(A: Vector or Matrix, B: Vector or Matrix) -> Vector or Matrix:
    """Matrix-vector/vector-matrix multiplication.
    
    Args:
        A (Vector or Matrix): The matrix represented as a list of lists.
        B (Vector or Matrix): The vector represented as a list.
    
    Returns:
        For Vector-Matrix Multiplication: A vector represented as a list.
        For Matrix-Vector Multiplication: A 1-column vector represented as a list of lists.
    
    Raises:
        ValueError: If the matrix and vector are not of compatible sizes.
    """
    
    mat_first = True
    try: (len(A[0]))
    except: mat_first = False

    if mat_first:
        row_a = len(A)
        col_a = len(A[0])
        row_b = len(B)

        if col_a != row_b:
            raise ValueError("Matrix must have as many columns as vector has rows.")
        
        out = [[None] for _ in range(row_a)]

        for i in range(row_a):
            sum = 0
            for j in range(row_b):
                sum += A[i][j] * B[j]
            out[i][0] = sum
        return out
    
    else:
        col_a = len(A)
        row_b = len(B)
        col_b = len(B[0])

        if col_a != row_b:
            raise ValueError("Matrix must have as many columns as vector has rows.")
        
        out = [None] * col_b

        for i in range(col_b):
            sum = 0
            for j in range(col_a):
                sum += A[j] * B[j][i]
            out[i] = sum
        return out