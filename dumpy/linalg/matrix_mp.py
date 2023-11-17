import multiprocessing as mp
from .matrix_core import matmul_core

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