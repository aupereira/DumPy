import random

def randrng(lb=0, ub=1, dtype='double'):
    """Returns a random scalar within a range."""
    if dtype == 'int':
        return int(random.random() * (ub - lb) // 1 + lb)
    elif dtype == 'double':
        return random.random() * (ub - lb) + lb
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")

def randvec(n, lb=0, ub=100, dtype='int'):
    """Returns a random vector of size n. Can choose int or double."""
    mul = ub - lb
    if dtype == 'int':
        return [int(random.random() * mul // 1 + lb) for i in range(n)]
    elif dtype == 'double':
        return [random.random() * mul + lb for i in range(n)]
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")

def randmat(r, c, lb=0, ub=100, dtype='int'):
    """Returns a random matrix of size r x c. Can choose int or double."""
    mul = ub - lb
    if dtype == 'int':
        return [[int(random.random() * mul // 1 + lb) for j in range(c)] for i in range(r)]
    elif dtype == 'double':
        return [[random.random() * mul + lb for j in range(c)] for i in range(r)]
    raise ValueError("Invalid dtype. Must be 'int' or 'double'.")