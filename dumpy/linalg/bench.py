from time import perf_counter
from .L3 import matmul
from .rand import randmat

def time_func(func,*args):
    t1 = perf_counter()
    func(*args)
    t2 = perf_counter()
    t = round(t2-t1,3)
    #print(f"{func} took {round(t2-t1,3)} seconds.")
    return(t)

def benchmark(size_a, size_b, mt=True):
    """Benchmarks floating point matrix multiplication of size n x m and m x n matrices."""
    A = randmat(size_a, size_b, dtype='double')
    B = randmat(size_b, size_a, dtype='double')

    flops = size_a * size_a * (size_b * 2 - 1)
    
    t = time_func(matmul, A, B)

    print(f"Time taken: {t}\nMFLOP/s: {round(flops * 1e-6 / t, 2)}")