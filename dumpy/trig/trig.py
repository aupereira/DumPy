from functools import cache

PI = 3.141592653589793

@cache
def inv_factorial(n):
    if n < 0:
        raise ValueError("Factorial of negative number.")
    v = 1
    for i in range(n, 1, -1):
        v *= i
    return v**-1

def taylor_sin(theta, iter=64):
    res = theta
    n = 3
    for i in range(0, iter):
        if i % 2 == 1:
            res += (theta ** n) * inv_factorial(n)
        else:
            res -= (theta ** n) * inv_factorial(n)
        n += 2
    return res

def taylor_cos(theta, iter=64):
    res = 1
    n = 2
    for i in range(0, iter):
        if i % 2 == 1:
            res += (theta ** n) * inv_factorial(n)
        else:
            res -= (theta ** n) * inv_factorial(n)
        n += 2
    return res