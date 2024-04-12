plus = lambda a, b: a + b
minus = lambda a, b: a - b
times = lambda a, b: a * b
divided_by = lambda a, b: a // b  # Use // for integer division

# Define functions for numbers one to nine using lambda with pre-defined values
one = lambda: 1
two = lambda: 2
three = lambda: 3
four = lambda: 4
five = lambda: 5
six = lambda: 6
seven = lambda: 7
eight = lambda: 8
nine = lambda: 9

# Example calculations
print(seven(times(five())))  # Output: 35
print(four(plus(nine())))  # Output: 13
print(eight(minus(three())))  # Output: 5
print(six(divided_by(two())))  # Output: 3
