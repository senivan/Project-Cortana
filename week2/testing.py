'''
This script has decorator functions to benchmark test
'''

import time
import tracemalloc

def time_to_run(func):
    '''
    This function acts as decorator to calculate a time needed to run the function
    '''
    def inner1(*args, **kwargs):
        res = 0
        for _ in range(1000):
            start_time = time.perf_counter()
            fin = func(*args, **kwargs)
            end_time = time.perf_counter()
            res += (end_time - start_time)
        print("Time taken:", func.__name__, res/1000)
        return fin
    return inner1

def memory_used(func):
    '''
    This function acts as decorator to calculate a memory used to run the function
    '''
    def inner2(*args, **kwargs):
        tracemalloc.start()
        res = func(*args, **kwargs)
        print("Memory:", func.__name__, tracemalloc.get_traced_memory())
        tracemalloc.stop()
        return res
    return inner2
