"""
Demonstrate higher order function - Timing another function
"""
import time


def timeit(func, args):
    """
    Prints the execution time of a function

    :param func: A function that should be timed
    :param args (list/tuple): Arguments of the function func
    :return: The return value of the function func
    """
    start = time.time()
    return_value = func(*args)
    end = time.time()
    print(f"Execution of function took {end-start} second(s)")
    return return_value


# Some dummy function that will be timed
def add(x, y):
    return x + y


print(add(1, 2))
# Using add as input for timeit
print(timeit(add, (1, 2)))
# Using lambda function
print(timeit(lambda x, y: x+y, (1, 2)))

