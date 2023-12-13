# Contains core linalg functions that return vectors.

def outer(v1, v2):
    """Computes the outer product of two vectors."""
    l1 = len(v1)
    l2 = len(v2)

    if l1 != l2:
        raise ValueError("Vectors must be of same length.")

    out = [[None] * l1 for _ in range(l1)]

    for i in range(l1):
        for j in range(l1):
            out[i][j] = v1[i] * v2[j]

    return out

def mvmul(A, B):
    """Matrix vector multiply. Returns a vector."""
    
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