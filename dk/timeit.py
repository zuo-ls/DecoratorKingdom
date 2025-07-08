import time

#decorator to measure the time it takes to run a function
def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start} seconds")
        return result
    return wrapper

#example usage
@timeit
def my_function():
    time.sleep(2)