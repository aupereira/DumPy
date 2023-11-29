# To-Do
# Should make it so that it selects to divide based on whichever array is bigger for mt. ###
# Extend rand functions to allow for a range of values (and make them multithreaded).
# Do proper 0D, 1D, 2D interoperability.
# Do that weird 2D*2D=4D thing.
# Do data validity checks.

# Maybe tensor operations.

import random
from .matrix_core import matmul_core, matmul_core_old
from .matrix_mp import matmul_mt

def flipmat(A):
    """Flips a matrix."""
    return [list(i) for i in zip(*A)]

def randvec(n, dtype='int'):
    """Returns a random vector of size n. Can choose int or double."""
    if dtype == 'int':
        return [int(random.random() * 100 // 1) for i in range(n)]
    elif dtype == 'double':
        return [random.random() * 100 for i in range(n)]
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")

def randmat(r, c, dtype='int'):
    """Returns a random matrix of size r x c. Can choose int or double."""
    if dtype == 'int':
        return [[int(random.random() * 100 // 1) for j in range(c)] for i in range(r)]
    elif dtype == 'double':
        return [[random.random() * 100 for j in range(c)] for i in range(r)]
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")

def matmul(A, B, mt=True, flip=True):
    if mt == True:
        return matmul_mt(A, flipmat(B))
    elif flip == True:
        return matmul_core(A, flipmat(B))
    return matmul_core_old(A, B)