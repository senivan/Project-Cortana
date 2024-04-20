"""This module contains functions for calculus."""
# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.
from collections.abc import Callable
from benchmark_funcs import time_to_run, memory_used

def find_max_1(function: Callable, points:list) -> float:
    """ 
    (function, list(number)) -> (number)
    
    Find and return maximal value of function f in points.
    
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12

    Time taken: find_max_1 1.2564001372084022e-06
    Memory: find_max_1 (0, 80)
    """
    res = []
    for num in points:
        res.append(function(num))
    return max(res)

def find_max_2(function: Callable, points:list) -> int:
    """ 
    (function, list(number)) -> (number)
    
    Find and return list of points where function f has the maximal value.
    
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]

    Time taken: find_max_2 4.914299352094531e-06
    Memory: find_max_2 (0, 160)
    """
    res = []
    for num in points:
        if function(num) == find_max_1(function, points):
            res.append(num)
    return res

def compute_limit(seq: Callable) -> float:
    """
    (function) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0

    Time taken: compute_limit 3.197200130671263e-06
    Memory: compute_limit (72, 297)
    """
    lst = []
    count = 0
    while True:
        val = 10 ** count
        lst.append(seq(val))
        if count != 0 and abs(lst[count] - lst[count - 1]) < 0.001:
            return float(f'{lst[count]:.1f}')
        count += 1

def compute_derivative(function:Callable, x_0:int) -> int:
    """
    (function, number) -> (number)
    
    Compute and return derivative of function f in the point x_0.
    
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0

    Time taken: compute_derivative 7.0490994257852435e-06
    Memory: compute_derivative (48, 243)
    """
    count = 0
    aprox = []
    while True:
        d_x = 10 ** -count
        val = x_0 + d_x
        d_f = function(val)
        val = x_0
        d_f -= function(val)
        der = d_f / d_x
        aprox.append(der)
        if count!= 0 and abs(aprox[count] - aprox[count-1]) < 0.001:
            return float(f'{aprox[count]:.2f}')
        count+= 1

def get_tangent(function: Callable, x_0: int) -> str:
    """
    (function, number) -> (str)
    
    Compute and return tangent line to function f in the point x_0.
    
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'

    Time taken: get_tangent 8.639200357720256e-06
    Memory: get_tangent (24, 276)
    """
    count= 0
    aprox = []
    while True:
        d_x = 10 ** - count
        val = x_0 + d_x
        d_f = function(val)
        val = x_0
        d_f -= function(val)
        der = d_f / d_x
        aprox.append(der)
        if count!= 0 and abs(aprox[count-1] - aprox[count- 2]) < 0.001:
            if aprox[count-1] < 0:
                if function(x_0)-aprox[count-1]*x_0 < 0:
                    return '- '+f'{abs(aprox[count-1]):.1f}'+' * x - '+(
                        f'{abs(function(x_0)-aprox[count-1]*x_0):.1f}')
                return '- '+f'{abs(aprox[count-1]):.1f}'+' * x + '+(
                    f'{abs(function(x_0)-aprox[count-1]*x_0):.1f}')
            if aprox[count-1] > 0:
                if function(x_0)-aprox[count-1]*x_0 < 0:
                    return f'{abs(aprox[count-1]):.1f}'+' * x - '+(
                        f'{abs(function(x_0)-aprox[count-1]*x_0):.1f}')
                return f'{abs(aprox[count-1]):.1f}'+' * x + '+(
                    f'{function(x_0)-aprox[count-1]*x_0:.1f}')
        count+= 1

def get_root(function: Callable, start: int, end:int) -> int:
    """
    (function, number, number) -> (number)
    
    Compute and return root of the function f in the interval (a, b).
    
    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: x ** 3, -100, 150)
    0.0

    Time taken: get_root 2.0895900321193038e-05
    Memory: get_root (0, 130)
    """
    while end-start >= 0.001:
        mid = (start+end)/2
        if function(mid) == 0:
            return float(f'{mid:.1f}')
        if function(start)*function(mid) >= 0:
            start = mid
        else:
            end = mid
    if float(f'{mid:.1f}') == 0.0:
        return 0.0
    return float(f'{mid:.1f}')

if __name__ == '__main__':
    find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    compute_derivative(lambda x: x**2 + x, 2)
    get_tangent(lambda x: x ** 2 + x, 2)
    get_root(lambda x: x**3, -100, 150)
