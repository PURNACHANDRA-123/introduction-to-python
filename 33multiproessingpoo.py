from multiprocessing import pool

def f(n):
    return n*n


if __name__ == "__main__":
    array=[1,2,3]
    p = pool.Pool(processes=2)
    print(p.map(f, array))



#process is argument of mapreduce








     