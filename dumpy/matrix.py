### Should make it so that it selects to divide based on whichever array is bigger for mt. ###

import random
from dumpy.matrix_core import matmul_core
from dumpy.matrix_mp import matmul_mt

def flipmat(A):
    """Flips a matrix."""
    return [list(i) for i in zip(*A)]

def randmat(r, c, dtype='int'):
    """Returns a random integer matrix of size r x c. Can choose int or double."""
    if dtype == 'int':
        return [[int(random.random() * 100 // 1) for j in range(c)] for i in range(r)]
    elif dtype == 'double':
        return [[random.random() * 100 for j in range(c)] for i in range(r)]
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")

def matmul(A, B, mt=True):
    if mt == True:
        return matmul_mt(A, B)
    else:
        return matmul_core(A, B)