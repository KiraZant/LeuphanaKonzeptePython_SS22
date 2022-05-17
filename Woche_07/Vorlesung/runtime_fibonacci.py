# -*- coding: utf-8 -*-
"""
Created on February 24 2021
Jonas Scharfenberger
ODHS1 - Effizienz von Algorithmen
Measuring the runtime of fibonacci functions
"""
import time


def slow_fibonacci(n):
    if n <= 2:
        return 1
    else:
        return slow_fibonacci(n-1) + slow_fibonacci(n-2)


def fast_fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a+b
    return a


def timeit(func, n_fib, n_runs):
    times = []
    for i in range(n_runs):
        start = time.time()
        _ = func(n_fib)
        end = time.time()
        times.append(end-start)
    avg_time = sum(times)/len(times)
    print(f'Function finished in {round(avg_time, 4)} second(s)')


timeit(slow_fibonacci, 30, 5)
timeit(fast_fibonacci, 3500, 5)
