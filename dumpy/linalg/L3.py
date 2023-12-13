# Contains core linalg functions that return matrices.

import multiprocessing as mp

type Matrix = list[list[float or int]]

def transpose(A: Matrix) -> Matrix:
    """Transposes a matrix.

    Args:
        A (Matrix): The matrix to be transposed.

    Returns:
        Matrix: The transposed matrix.
    """

    return [list(i) for i in zip(*A)]

def identity(n: int) -> Matrix:
    """Returns an identity matrix of size n x n.

    Parameters:
        n (int): The size of the identity matrix.

    Returns:
        Matrix: The identity matrix of size n x n.
    """

    A = [[0]*n for _ in range(n)]
    for i in range(n):
        A[i][i] = 1
    return A

def matadd(A: Matrix, B: Matrix) -> Matrix:
    """Adds two matrices.

    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix.

    Returns:
        Matrix: The resulting matrix after adding A and B.
    """

    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        res.append(row)
    return res

def matsub(A: Matrix, B: Matrix) -> Matrix:
    """Subtracts two matrices.

    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix.

    Returns:
        Matrix: The resulting matrix after subtracting B from A.
    """

    res = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] - B[i][j])
        res.append(row)
    return res

def matmul_core(A: Matrix, B: Matrix, list=None) -> Matrix:
    """Performs a single-threaded matrix multiplication on two matrices.
    
    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix. Matrix must be transposed prior to multiplication.
        list (list, optional): A list to extend the result matrix. Defaults to None.
    
    Returns:
        Matrix: The result of the matrix multiplication.
    """

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

def matmul_core_no_trans(A: Matrix, B: Matrix, list=None) -> Matrix:
    """Performs a single-threaded matrix multiplication on two matrices.
    
    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix.
        list (list, optional): A list to extend the result matrix. Defaults to None.
    
    Returns:
        Matrix: The result of the matrix multiplication.
    """

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

def matmul_mt(A: Matrix, B: Matrix) -> Matrix:
    """(Very basic) multithreaded scheduler for matrix multiplcation.
    
    Avoids recursively spawning processes because Python dosen't support proper threading.

    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix.

    Returns:
        Matrix: The result of matrix multiplication.
    """

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

def matmul(A: Matrix, B: Matrix, mt: bool =True, flip: bool =True) -> Matrix:
    """Performs a matrix multiplication on two matrices.

    Args:
        A (Matrix): The first matrix.
        B (Matrix): The second matrix.
        mt (Bool, optional): Flag indicating whether to use multithreaded implementation. Defaults to True.
        flip (Bool, optional): Flag indicating whether to transpose the second matrix. Defaults to True. Not available for multithreaded implementation.

    Returns:
        Matrix: The result of the matrix multiplication.
    """

    if mt == True:
        return matmul_mt(A, transpose(B))
    elif flip == True:
        return matmul_core(A, transpose(B))
    return matmul_core_no_trans(A, B)