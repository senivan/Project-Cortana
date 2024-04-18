def zero():
  """Returns the number zero"""
  return 0

def one():
  """Returns the number one"""
  return 1

def two():
  """Returns the number two"""
  return 2

def three():
  """Returns the number three"""
  return 3

def four():
  """Returns the number four"""
  return 4

def five():
  """Returns the number five"""
  return 5

def six():
  """Returns the number six"""
  return 6

def seven():
  """Returns the number seven"""
  return 7

def eight():
  """Returns the number eight"""
  return 8

def nine():
  """Returns the number nine"""
  return 9

# Define functions for operations using lambda expressions
plus = lambda a, b: a + b
minus = lambda a, b: a - b
times = lambda a, b: a * b
divided_by = lambda a, b: a // b  # Use // for integer division

# Example calculations
print(seven(times(five())))  # Output: 35
print(four(plus(nine())))  # Output: 13
print(eight(minus(three())))  # Output: 5
print(six(divided_by(two())))  # Output: 3
