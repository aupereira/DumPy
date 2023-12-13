import random

type Scalar = float or int
type Vector = list[float or int]
type Matrix = list[Vector]

def randrng(lb: Scalar =0, ub: Scalar =1, dtype: str ='float') -> Scalar:
    """Returns a random scalar within a specified range.

    Please don't use this for random ints, esecially for small ranges.
    Use a builtin like random.randint() instead.

    Parameters:
        lb (Scalar, optional): The lower bound of the range (inclusive). Default is 0.
        ub (Scalar, optional): The upper bound of the range (inclusive). Default is 1.
        dtype (Scalar, optional): The data type of the returned scalar. Must be 'int' or 'float'. Default is 'float'.

    Returns:
        Scalar: A random scalar within the specified range.

    Raises:
        ValueError: If the dtype is not 'int' or 'double'.
    """

    if dtype == 'int':
        return int(random.random() * (ub - lb) // 1 + lb)
    elif dtype == 'float':
        return random.random() * (ub - lb) + lb
    raise ValueError("Invalid dtype. Must be 'int' or 'float.'")

def randvec(n: int, lb: Scalar =0, ub: Scalar =100, dtype: str ='float') -> Vector:
    """Returns a random vector of size n.

    Please don't use this for random ints, esecially for small ranges.
    Use a builtin like random.randint() instead.

    Parameters:
        n (int): The size of the vector.
        lb (Scalar, optional): The lower bound of the random values. Defaults to 0.
        ub (Scalar, optional): The upper bound of the random values. Defaults to 100.
        dtype (str, optional): The data type of the random values. Can be 'int' or 'float'. Defaults to 'float'.

    Returns:
        Vector: The random vector.

    Raises:
        ValueError: If the dtype is not 'int' or 'float'.
    """

    mul = ub - lb
    if dtype == 'int':
        return [int(random.random() * mul // 1 + lb) for i in range(n)]
    elif dtype == 'float':
        return [random.random() * mul + lb for i in range(n)]
    raise ValueError("Invalid dtype. Must be 'int' or 'float.'")

def randmat(r: int, c: int, lb: Scalar =0, ub: Scalar =100, dtype: str ='float') -> Matrix:
    """Returns a random matrix of size r x c.

    Please don't use this for random ints, esecially for small ranges.
    Use a builtin like random.randint() instead.

    Parameters:
        r (int): The number of rows of the output matrix.
        c (int): The number of columns of the output matrix.
        lb (Scalar, optional): The lower bound of the random values. Defaults to 0.
        ub (Scalar, optional): The upper bound of the random values. Defaults to 100.
        dtype (str, optional): The data type of the random values. Can be 'int' or 'float'. Defaults to 'float'.

    Returns:
        Matrix: The random matrix.

    Raises:
        ValueError: If the dtype is not 'int' or 'float'.
    """

    mul = ub - lb
    if dtype == 'int':
        return [[int(random.random() * mul // 1 + lb) for j in range(c)] for i in range(r)]
    elif dtype == 'float':
        return [[random.random() * mul + lb for j in range(c)] for i in range(r)]
    raise ValueError("Invalid dtype. Must be 'int' or 'float.'")