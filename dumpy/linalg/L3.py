# Contains core linalg functions that return matrices.

import multiprocessing as mp

def transpose(A):
    """Flips a matrix."""
    return [list(i) for i in zip(*A)]

def identity(n):
    """Returns an identity matrix of size n x n."""
    A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = 1
    return A

def matadd(A, B):
    """Adds two matrices."""
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        res.append(row)
    return res

def matsub(A, B):
    """Subtracts two matrices."""
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        res.append(row)
    return res

def matmul_core(A, B, list=None):
    """Performs a matrix multiplication on two matrices.
    \nExploits spatial locality by transposing the second matrix."""
    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(B)):
            sum = 0
            for k in range(len(A[0])):
                sum += A[i][k] * B[j][k]
            row.append(sum)
        res.append(row)
    if list == None:
        return res
    list.extend(res)

def matmul_core_no_trans(A, B, list=None):
    """Performs a matrix multiplication on two matrices."""
    res = []
    for r in range(len(A)):
        row = []
        for c in range(len(B[0])):
            sum = 0
            for i in range(len(A[0])):
                sum += A[r][i] * B[i][c]
            row.append(sum)
        res.append(row)
    if list == None:
        return res
    list.extend(res)

def matmul_mt(A, B):
    """(Very basic) multithreaded scheduler for matmul_core."""
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
    res = manager.list([])

    processes = []

    if len_A > threads:
        for i in range(0,threads):
            processes.append(mp.Process(
                target=matmul_core, args=(
                    A[thread_indexes[i]:thread_indexes[i+1]], B, res
                )
            ))
            processes[i].start()
    else:
        for i in range(0,len_A):
            processes.append(mp.Process(target=matmul_core, args=(A[i:i+1], B, res)))
            processes[i].start()
    
    for i in range(len(processes)):
        processes[i].join()
    
    return list(res)

def matmul(A, B, mt=True, flip=True):
    """Performs a matrix multiplication on two matrices. Defaults to multithreaded implementation."""
    if mt == True:
        return matmul_mt(A, transpose(B))
    elif flip == True:
        return matmul_core(A, transpose(B))
    return matmul_core_no_trans(A, B)