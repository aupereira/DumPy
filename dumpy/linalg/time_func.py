from time import perf_counter

def time_func(func,*args):
    t1 = perf_counter()
    func(*args)
    t2 = perf_counter()
    t = round(t2-t1,3)
    print(f"{func} took {round(t2-t1,3)} seconds.")
    return(t)