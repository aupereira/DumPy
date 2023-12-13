from functools import cache

PI = 3.141592653589793

@cache
def inv_factorial(n: int) -> int or float:
    """Calculates the inverse factorial of a non-negative integer.

    Parameters:
        n (int): The non-negative integer for which to calculate the inverse factorial.

    Returns:
        float: The inverse factorial of the given integer.

    Raises:
        ValueError: If the input is a negative number.
        ValueError: If the input is not an integer.
    """

    if n < 0:
        raise ValueError("Factorial of negative number.")
    if type(n) != int:
        raise ValueError("Factorial of non-integer.")
    v = 1
    for i in range(n, 1, -1):
        v *= i
    return v**-1

def taylor_sin(theta: float or int, iter: int =64) -> float or int:
    """Calculate the sine of an angle using Taylor series approximation.

    Parameters:
        theta (float or int): The angle in radians.
        iter (int): The number of iterations to perform in the Taylor series approximation. Default is 64.

    Returns:
        float or int: The sine of the angle.
    """

    res = theta
    n = 3
    for i in range(0, iter):
        if i % 2 == 1:
            res += (theta ** n) * inv_factorial(n)
        else:
            res -= (theta ** n) * inv_factorial(n)
        n += 2
    return res

def taylor_cos(theta: float or int, iter: int =64) -> float or int:
    """Calculate the cosine of an angle using Taylor series approximation.

    Parameters:
        theta (float or int): The angle in radians.
        iter (int): The number of iterations to perform in the Taylor series approximation. Default is 64.

    Returns:
        float or int: The cosine of the angle.
    """

    res = 1
    n = 2
    for i in range(0, iter):
        if i % 2 == 1:
            res += (theta ** n) * inv_factorial(n)
        else:
            res -= (theta ** n) * inv_factorial(n)
        n += 2
    return res