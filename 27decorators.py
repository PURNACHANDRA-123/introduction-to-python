import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start} seconds")
        return result
    return wrapper 




@time_it
def calc_square(numbers):
    result= []
    for num in numbers:
        result.append(num*num)
    return result

@time_it
def calc_cube(numbers):
    result= []
    for num in numbers:
        result.append(num*num*num)
    return result

arr=range(1,100000)
calc_sq=calc_square(arr)
calc_cub=calc_cube(arr)



















