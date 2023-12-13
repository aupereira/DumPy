# Contains core linalg functions that return scalars.

from math import sqrt

def inner(v1, v2):
    """Computes the inner product of two vectors."""
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

def norm(v, p=2):
    """Computes the p-norm of a vector. Default is Euclidean (2nd) norm."""
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