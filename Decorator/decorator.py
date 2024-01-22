import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'result in function: {result}')
        print(f'{func.__name__} took {int((end - start) * 1000)}ms')

    return wrapper


@timer
def fibonacci(n):
    f1 = f2 = 1
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
    time.sleep(1)
    return 'fibonacci(' + str(n) + ')=' + str(f2)


@timer
def foo():
    time.sleep(1)
    return 'the function foo() is completed'


print(fibonacci(15))
print(foo())