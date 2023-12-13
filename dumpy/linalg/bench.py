from time import perf_counter
from .L3 import matmul
from .rand import randmat

def time_func(func, *args) -> float:
    """Measures the execution time of a function.

    Parameters:
        func: The function to be timed.
        *args: Arguments to be passed to the function.

    Returns:
        float: The execution time in seconds.
    """

    t1 = perf_counter()
    func(*args)
    t2 = perf_counter()
    t = round(t2 - t1, 3)
    #print(f"{func} took {round(t2-t1,3)} seconds.")
    return t

def benchmark(a: int, b: int, mt: bool =True):
    """Benchmarks floating point matrix multiplication of size n x m and m x n matrices.

    Parameters:
        a (int): The number of rows in matrix A and the number of columns in matrix B.
        b (int): The number of columns in matrix A and the number of rows in matrix B.
        mt (bool, optional): Flag indicating whether to use multithreading. Defaults to True.

    Returns:
        None
    """

    A = randmat(a, b, dtype='double')
    B = randmat(b, a, dtype='double')

    flops = a * a * (b * 2 - 1)
    
    t = time_func(matmul, A, B)

    print(f"Time taken: {t}\nMFLOP/s: {round(flops * 1e-6 / t, 2)}")