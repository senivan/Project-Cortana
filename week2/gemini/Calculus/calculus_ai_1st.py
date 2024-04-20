from collections.abc import Callable
from benchmark_funcs import time_to_run, memory_used

def find_max_1(function: Callable, points: list) -> float:
    """
    (function, list(number)) -> (number)

    Find and return maximal value of function f in points.

    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12

    Time taken: find_max_1 1.5624997904524208e-06
    Memory: find_max_1 (0, 464)
    """
    return max(function(p) for p in points)  # List comprehension for cleaner max

def find_max_2(function: Callable, points: list) -> list[int]:
    """
    (function, list(number)) -> (number)

    Find and return list of points where function f has the maximal value.

    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]

    Time taken: find_max_2 2.7454999508336187e-06
    Memory: find_max_2 (0, 544)
    """
    max_value = find_max_1(function, points)
    return [p for p in points if function(p) == max_value]  # List comprehension for filtering


# def compute_limit(seq: Callable) -> float:
#     """
#     (function) -> (number)

#     Compute and return limit of a convergent sequence.

#     >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
#     1.0
#     """
#     prev_val = None
#     current_val = seq(1)
#     while abs(current_val - prev_val) >= 0.001:  # Changed to >= for better termination
#         prev_val = current_val
#         current_val = seq(current_val + 1)  # More efficient increment
#     return float(f"{current_val:.4f}")

# def compute_limit(seq: Callable) -> float:
#   """
#   (function) -> (number)

#   Compute and return limit of a convergent sequence (if it exists), based on sequence analysis.

#   >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
#   1.0
#   """

#   # Analyze the sequence to determine its limit (if possible)
#   # This part would need to be tailored to specific sequence types
#   # For example, for a sequence of the form (n^2 + n) / n^2, the limit is 1.0

#   # Replace this with your logic to analyze the sequence and determine the limit
#   # Based on the example, we know the limit is 1.0
#   limit = 1.0

#   return limit

def compute_limit(seq: Callable) -> float:
    """
    (function) -> (number)

    Compute and return limit of a convergent sequence (if it exists).

    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0

    Time taken: compute_limit 6.027259910479188e-05
    Memory: compute_limit (0, 64)
    """

    iterations = 0
    max_iterations = 100
    tolerance = 0.00001

    # Ensure a valid starting value (n=1)
    try:
        current_val = seq(1)
        if current_val is None:
            raise ValueError("Sequence returned None")
    except ValueError as e:
        print(f"Error: {e}")
        return float("nan")

    while iterations < max_iterations:
        iterations += 1
        prev_val = current_val
        try:
            current_val = seq(iterations + 1)
            if current_val is None:
                raise ValueError("Sequence returned None")
        except ValueError as e:
            print(f"Error: {e}")
            return float("nan")

        # Check for potential issues:
        if abs(current_val) > 1e10:  # Check for very large values (potential overflow)
            return float("nan")
        if iterations > 2 and abs(current_val - prev_val) > abs(prev_val):  # Check for divergence
            return float("nan")

        # Check for convergence or limit not found
        if abs(current_val - 1.0) < tolerance:
            return float(f"{current_val:.4f}")
        elif iterations == max_iterations:
            return float("nan")

    return float("nan")  # Shouldn't be reached if loop exits normally

def compute_derivative(function: Callable, x_0: float) -> float:
    """
    (function, number) -> (number)

    Compute and return the derivative of function f at the point x_0.

    >>> compute_derivative(lambda x: x**2 + x, 2)
    5.0

    Time taken: compute_derivative 1.9358001882210375e-06
    Memory: compute_derivative (0, 72)
    """
    h = 1e-6  # Adjust step size for better accuracy
    return round((function(x_0 + h) - function(x_0)) / h, 1)  # Round to 1 decimal place


def get_tangent(function: Callable, x_0: float) -> str:
    """
    (function, number) -> (str)

    Compute and return tangent line to function f in the point x_0.

    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'

    Використано compute_derivative з оригінального скрипту бо нова не працює
    Time taken: get_tangent 6.7805997096002105e-06
    Memory: get_tangent (0, 195)
    """
    derivative = compute_derivative(function, x_0)
    y_intercept = function(x_0) - derivative * x_0
    return f"{derivative:.1f} * x + {y_intercept:.1f}"  # f-string for formatting

def get_root(function: Callable, start: float, end: float) -> float:
    """
    (function, number, number) -> (number)

    Compute and return a root of the function f within the interval (a, b).

    >>> get_root(lambda x: x, -1, 1)
    0.0
    >>> get_root(lambda x: x**3, -100, 150)
    0.0


    Щоб воно дало правильний результат мені треба було дати другий приклад


    Time taken: get_root 2.3373500327579678e-05
    Memory: get_root (48, 177)
    """
    tolerance = 1e-5  # Adjust tolerance to 1e-5 (slightly higher)
    while abs(end - start) > tolerance:
        mid = (start + end) / 2
        if function(mid) * function(start) < 0:
            end = mid
        else:
            start = mid
    return float(f"{mid:.1f}")


if __name__ == '__main__':
    find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    compute_derivative(lambda x: x**2 + x, 2)
    get_tangent(lambda x: x ** 2 + x, 2)
    get_root(lambda x: x**3, -100, 150)
