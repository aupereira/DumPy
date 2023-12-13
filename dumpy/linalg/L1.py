# Contains core linalg functions that return scalars.

from math import sqrt

type Scalar = float or int
type Vector = list[float or int]

def inner(v1: Vector, v2: Vector) -> Scalar:
    """Computes the inner product of two vectors.

    Args:
        v1 (Vector): The first vector.
        v2 (Vector): The second vector.

    Returns:
        Scalar: The inner product of the two vectors.
    """

    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

def norm(v: Vector, p: int =2) -> Scalar:
    """Computes the p-norm of a vector.

    Parameters:
        v (Vector): The input vector.
        p (int, optional): The order of the norm. Default is 2 (Euclidean norm).

    Returns:
        Scalar: The p-norm of the vector.
    """

    if p == 2:
        total = 0
        for i in range(len(v)):
            total += v[i]**2
        return sqrt(total)
    elif p == 1:
        return sum([abs(i) for i in v])
    elif p == float('inf'):
        return max([abs(i) for i in v])
    else:
        total = 0
        for i in range(len(v)):
            total += abs(v[i])**p
        return total**(1/p)