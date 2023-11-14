### Should make it so that it selects to divide based on whichever array is bigger for mt. ###

import multiprocessing as mp
import random
from time import perf_counter

def randmat(r, c, dtype='int'):
    """Returns a random integer matrix of size r x c. Can choose int or double."""
    if dtype == 'int':
        return [[int(random.random() * 100 // 1) for j in range(c)] for i in range(r)]
    elif dtype == 'double':
        return [[random.random() * 100 for j in range(c)] for i in range(r)]
    raise valueError("Invalid dtype. Must be 'int' or 'double'.")

def time_func(func,*args):
    t1 = perf_counter()
    func(*args)
    t2 = perf_counter()
    t = round(t2-t1,3)
    print(f"{func} took {round(t2-t1,3)} seconds.")
    return(t)

# Fastest singlethreaded implementation based on testing.
def matmul_st(A, B):
    output = []
    for r in range(len(A)):
        row = []
        for c in range(len(B[0])):
            sum = 0
            for i in range(len(A[0])):
                sum += A[r][i] * B[i][c]
            row.append(sum)
        output.append(row)
    return(output)

# Fastest multithreaded implementation based on testing.
def matmul_mt_core(A, B, output):
    final = []
    for r in range(len(A)):
        row = []
        for c in range(len(B[0])):
            sum = 0
            for i in range(len(A[0])):
                sum += A[r][i] * B[i][c]
            row.append(sum)
        final.append(row)
    output.extend(final)

# Process manager for multithreaded matrix multiply.
def matmul_mt(A, B):
    len_A = len(A)
    threads = mp.cpu_count()

    thread_rows = len_A // threads
    extra_row_threads = len_A % threads

    thread_indexes = [0]
    for i in range(1,threads+1):
        thread_indexes.append(thread_rows*i)
        if extra_row_threads > i:
            thread_indexes[i] += i
        else:
            thread_indexes[i] += extra_row_threads

    manager = mp.Manager()
    output = manager.list([])

    processes = []

    if len_A > threads:
        for i in range(0,threads):
            processes.append(mp.Process(target=matmul_mt_core, args=(A[thread_indexes[i]:thread_indexes[i+1]],B,output)))
            processes[i].start()
    else:
        for i in range(0,len_A):
            processes.append(mp.Process(target=matmul_mt_core, args=(A[i:i+1],B,output)))
            processes[i].start()
    
    for i in range(len(processes)):
        processes[i].join()
    
    return output

def main():
    A = randmat(1200,1000)
    B = randmat(1000,1200)

    st = time_func(matmul_st,A,B)
    mt = time_func(matmul_mt,A,B)

    mt_ratio = round(st/mt,2)

    print(f"Multithreaded Speedup Ratio: {mt_ratio}")

if __name__ == "__main__":
    main()