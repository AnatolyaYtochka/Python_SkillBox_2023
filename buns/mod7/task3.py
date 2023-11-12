import functools
import time

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = end - start
        print(f"Функция {func.__name__} работала {run_time} секунд")
        return result
    return wrapper


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timer
def run_fibonacci(n):
    print(fibonacci(n))

run_fibonacci(20)


def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@timer
def run_fibonacci_with_memoize(n):
    print(fibonacci(n))

run_fibonacci_with_memoize(20)
