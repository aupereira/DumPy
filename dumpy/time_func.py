from time import perf_counter

def time_func(func,*args):
    t1 = perf_counter()
    func(*args)
    t2 = perf_counter()
    t = round(t2-t1,3)
    print(f"{func} took {round(t2-t1,3)} seconds.")
    return(t)

# def main():
#     A = randmat(1200,1000)
#     B = randmat(1000,1200)

#     st = time_func(matmul_st,A,B)
#     mt = time_func(matmul_mt,A,B)

#     mt_ratio = round(st/mt,2)

#     print(f"Multithreaded Speedup Ratio: {mt_ratio}")

# if __name__ == "__main__":
#     main()